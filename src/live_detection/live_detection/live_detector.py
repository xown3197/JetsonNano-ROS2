'''Copyright (c) 2019-2020, NVIDIA CORPORATION. All rights reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.'''

import sys
import argparse

import rclpy

from live_detection.live_detection_helper import DetectionNode

def main(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '-P',
        '--ckpt-path',
        type=str,
        default='content/tmp3',
        help='Chekcpoint path'
        )
    parser.add_argument(
        'argv',
        nargs=argparse.REMAINDER,
        help='Pass arbitrary arguments ti the executable'
        )
    args = parser.parse_args()
    
    rclpy.init(args=args.argv)

    detection_node = DetectionNode(args=args)

    rclpy.spin(detection_node)

    detection_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
