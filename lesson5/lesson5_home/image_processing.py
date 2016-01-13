import os
from PIL import Image

def resize_image(path_image,dir, filename):
    try:
        img = Image.open(path_image)
        wigth, height = img.size
        new_img = img.resize((wigth/2, height/2), Image.ANTIALIAS)
        new_img.save(dir+'/resized_' + filename)

    except:
        pass
if __name__ == "__main__":
    tree = os.walk(os.getcwd())
    for dirpath, dirname, filename in tree:
        for name in filename:
            resize_image(os.path.join(dirpath, name), dirpath, name)
        #print(dirpath, dirname, filename)
