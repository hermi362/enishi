# Reduce all JPEGs in a directory (and its subdirs)
# H.Gonzalez 2020/12
# Installation: Install python 3.x, including pip.
    # > python3 -m pip install --upgrade pip
    # > python3 -m pip install --upgrade Pillow


import PIL
from PIL import Image
import os
import os.path
import sys

def visitDir(path):
    # list all files and dirs in path
    for f in os.listdir(path):
        pf = os.path.join(path, f)
        if os.path.isdir(pf):
            print("-- Entering directory %s" % pf)
            visitDir(pf)
        else:
            if f.lower().endswith('.jpg') or f.lower().endswith('.jpeg'):
                shrinkJPEG(pf)

def shrinkJPEG(f_img):
    print("   Resizing %s ..." % f_img)
    # TODO: find a way to ignore .jpg files that do not contain JPEG data (e.g. corrupted files)

    img = Image.open(fp=f_img, formats=['JPEG'])
    if img.width <= 1280:
        print("** NOT OVER 1280 PIXELS WIDE, IGNORING: %s" % f_img)
        return

    exif = b''  # init with an empty bytearray
    if 'exif' in img.info:
        exif = img.info['exif']   # get exif_data
    img = img.resize((1280,960))

    stat_result = os.stat(f_img)  # get modification time
    mtime = stat_result.st_mtime

    img.save(f_img, exif=exif, optimize=True, quality=85)
    # NOTE: saving EXIF data like this means that the new reduced resolution is NOT in the EXIF data.
    
    img.close()  # close underlying jpg file if not already closed
    os.utime(f_img, (mtime, mtime)) # preserve modification time (as time of shot)




if __name__ == "__main__":
    for path in [r'c:\tmp\resize-us', r'']:
        visitDir(path)



