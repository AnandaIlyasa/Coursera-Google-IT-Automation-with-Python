#!/usr/bin/env python3

from PIL import Image
import glob
from os import path

SOURCE_PATH = "./supplier-data/images/"

def get_images(path):
    images = glob.glob(path + '*.tiff')
    return images

def resize_and_change_format(images, size, dest_path):
    for im_name in images:
        im = Image.open(im_name)
        resized_im = im.resize(size)
        rgb_im = resized_im.convert('RGB')
        rgb_im.save(dest_path + path.basename(im_name).split(".")[0] + ".jpeg")
        im.close()

def main():
    try:
        images = get_images(SOURCE_PATH)
        resize_and_change_format(images, (600, 400), SOURCE_PATH)
    except Exception as e:
        print("Fail : {}".format(e))

if __name__ == "__main__":
    main()