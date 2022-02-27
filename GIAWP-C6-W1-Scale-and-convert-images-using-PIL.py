#!/usr/bin/env python3

from PIL import Image
import glob

SOURCE_PATH = "./images/"
DEST_PATH = "/opt/icons/"

def get_images(path):
    images = glob.glob(path + '*')
    return images

def transform_and_save_images(images, size, rotation, dest_path):
    counter = 1
    for im_name in images:
        im = Image.open(im_name)
        result = im.resize(size).rotate(rotation)
        rgb_result = result.convert('RGB')
        rgb_result.save(dest_path + "icon" + str(counter) + ".jpeg")
        counter += 1
        im.close()

def main():
    images = get_images(SOURCE_PATH)
    transform_and_save_images(images, (128, 128), -90, DEST_PATH)

if __name__ == "__main__":
    main()