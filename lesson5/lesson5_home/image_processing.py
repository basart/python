import os
from PIL import Image
import sys


def resize_image(path_image, dir, filename):
    try:
        img = Image.open(path_image)
        wigth, height = img.size
        new_img = img.resize((wigth/2, height/2), Image.ANTIALIAS)
        new_img.save(dir+'/resized_' + filename)
        print("{} edited".format(filename))
    except IOError:
        print("{} isn't an image".format(filename))
if __name__ == "__main__":
    path_dir = sys.argv[1]
    tree = os.walk(path_dir)
    for dirpath, dirname, filename in tree:
        for name in filename:
            resize_image(os.path.join(dirpath, name), dirpath, name)

