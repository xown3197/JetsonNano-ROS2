import matplotlib
import matplotlib.pyplot as plt

import os
import random
import io
import glob
import argparse
from six import BytesIO

import scipy.misc
import numpy as np

from PIL import Image, ImageDraw, ImageFont

import tensorflow as tf

from utils import download_and_resize_image, show_inference

image_urls = [
  # Source: https://commons.wikimedia.org/wiki/File:The_Coleoptera_of_the_British_islands_(Plate_125)_(8592917784).jpg
  "https://upload.wikimedia.org/wikipedia/commons/1/1b/The_Coleoptera_of_the_British_islands_%28Plate_125%29_%288592917784%29.jpg",
  # By Amrico Toledano, Source: https://commons.wikimedia.org/wiki/File:Biblioteca_Maim%C3%B3nides,_Campus_Universitario_de_Rabanales_007.jpg
  "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Biblioteca_Maim%C3%B3nides%2C_Campus_Universitario_de_Rabanales_007.jpg/1024px-Biblioteca_Maim%C3%B3nides%2C_Campus_Universitario_de_Rabanales_007.jpg",
  # Source: https://commons.wikimedia.org/wiki/File:The_smaller_British_birds_(8053836633).jpg
  "https://upload.wikimedia.org/wikipedia/commons/0/09/The_smaller_British_birds_%288053836633%29.jpg",
  ]

def main(args):
    print("HELLOW WORLD!")

    new_model=tf.saved_model.load(args.ckpt_path)
    detections= new_model.signatures[ 'detect' ](tf.convert_to_tensor(np.ones([1,320,320,3]), dtype=tf.float32))
    print(detections.keys())
    
    image_path = download_and_resize_image(image_urls[1], 640, 480)

    img, _ = show_inference(new_model, image_path=image_path)

    img.show()
    

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Argparse Tutorial')
    parser.add_argument('--ckpt_path', type=str, 
                    help='It refers to checkpoint path of pretrained-model')
    parser.add_argument('--url', action='store_true')
    
    args = parser.parse_args()

    main(args)
