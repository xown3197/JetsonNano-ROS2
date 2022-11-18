'''Copyright (c) 2019-2020, NVIDIA CORPORATION. All rights reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.'''


# ROS2 imports 
import rclpy
from rclpy.node import Node

import tensorflow as tf

# CV Bridge and message imports
from sensor_msgs.msg import Image
from std_msgs.msg import String
from vision_msgs.msg import ObjectHypothesisWithPose, BoundingBox2D, Detection2D, Detection2DArray
from cv_bridge import CvBridge, CvBridgeError
import cv2

from live_detection.misc import Timer

import numpy as np
import os

from live_detection.live_detection import utils


class DetectionNode(Node):

    def __init__(self, args):
        super().__init__('detection_node')

        # Create a subscriber to the Image topic
        self.subscription = self.create_subscription(Image, 'image', self.listener_callback, 10)
        self.subscription  # prevent unused variable warning
        self.bridge = CvBridge()

        # Create a Detection 2D array topic to publish results on
        # self.detection_publisher = self.create_publisher(Detection2DArray, 'detection', 10)

        # Create an Image publisher for the results
        self.result_publisher = self.create_publisher(Image,'detection_image',10)

        # Model load
        self.new_model = tf.saved_model.load(args.ckpt_path)
        self.detections = self.new_model.signatures[ 'detect' ](tf.convert_to_tensor(np.ones([1,320,320,3]), dtype=tf.float32))
        print(self.detections.keys())

        self.timer = Timer()

    def listener_callback(self, data):
        self.get_logger().info("Received an image! ")
        try:
          cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
          print(e)

        
        image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
        self.timer.start()

        imgae, output_dict = utils.show_inference(self.new_model, img=image)
        
        interval = self.timer.end()

        print('Time: {:.2f}s.'.format(interval))

        cv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        cv2.imshow('object_detection', cv_image)
        # Publishing the results onto the the Detection2DArray vision_msgs format
        # self.detection_publisher.publish(detection_array)
        ros_image = self.bridge.cv2_to_imgmsg(cv_image)
        ros_image.header.frame_id = 'camera_frame'
        self.result_publisher.publish(ros_image)
        cv2.waitKey(1)
        


