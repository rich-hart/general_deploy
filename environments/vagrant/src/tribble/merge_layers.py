import os
from os.path import dirname, realpath, join
import unittest
import argparse
import json
import numpy
import cv2
import cv
DATA_DIR = join(dirname(realpath(__file__)),'data')
RESOURCE_DIR = join(DATA_DIR,'resources')
FAN_PICTURE = os.path.join(RESOURCE_DIR, 'FAN-PIC.png')
BACKGROUND_WALL = join(RESOURCE_DIR,'background_wall.png')
BACKGROUND_TRIBBLES = join(RESOURCE_DIR,'background_tribbles.png')
FORGROUND_TRIBBLES = join(RESOURCE_DIR,'forground_tribbles.png')
FORGROUND_BORDER_AND_LOGO = join(RESOURCE_DIR,'forground_border_and_logo.png')
OUTPUT = join(RESOURCE_DIR, 'merged_images.png')

def main(argv=None):
    import ipdb; ipdb.set_trace()
    parser = argparse.ArgumentParser(
        description='Return a list of related pages between two pdfs.')
    parser.add_argument('layers', type=str,  nargs='+')
    parser.add_argument('--output', type=argparse.FileType('wb+'), default = 'merged_images.png')
   
    args = parser.parse_args(argv)
    settings = vars(args)
    layers = settings['layers']
    total_layers = len(layers)
    img1 = cv2.imread(BACKGROUND_WALL,-1)
#    rows,cols,channels = img1.shape
#    channel = numpy.ones([rows,cols])
#    img1=numpy.append(arr=img1,values=channel,axis=2)
#    img1[:,:,4]=channel
#    for layer in layers:

    img2 = cv2.imread(BACKGROUND_TRIBBLES,-1)

#        img = cv2.imread(layer)
#        dst = cv2.addWeighted(final_img,0.5,img,0.5,1.0/float(total_layers)) 
#        final_img = dst
#    cv2.imwrite(settings['output'].name,final_img)

    # Load two images
#    img1 = cv2.imread('messi5.jpg')
#    img2 = cv2.imread('opencv-logo.png')
    # I want to put logo on top-left corner, So I create a ROI
    rows,cols,channels = img2.shape
    roi = img1[0:rows, 0:cols ]
    # Now create a mask of logo and create its inverse mask also
    img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    # Now black-out the area of logo in ROI
    img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
    # Take only region of logo from logo image.
    img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
    # Put logo in ROI and modify the main image
    dst = cv2.add(img1_bg,img2_fg)
    img1[0:rows, 0:cols ] = dst
#    cv2.imshow('res',img1)
    cv2.imwrite(settings['output'].name,img1) 
    return settings



DATA_DIR = join(dirname(realpath(__file__)),'data')
TEST_DATA = join(DATA_DIR,'resources')
TEST_FAN_PICTURE = os.path.join(TEST_DATA, 'FAN-PIC.png')
TEST_BACKGROUND_WALL = join(TEST_DATA,'background_wall.jpg')
TEST_BACKGROUND_TRIBBLES = join(TEST_DATA,'background_tribbles.png')
TEST_FORGROUND_TRIBBLES = join(TEST_DATA,'forground_tribbles.png')
TEST_FORGROUND_BORDER_AND_LOGO = join(TEST_DATA,'forground_border_and_logo.png')
TEST_OUTPUT = join(TEST_DATA, 'merged_images.png')

class TestTribbify(unittest.TestCase):
 
    def test(self):
        pass

    def test_main(self):
        main([TEST_BACKGROUND_WALL,TEST_BACKGROUND_TRIBBLES,TEST_FAN_PICTURE,TEST_FORGROUND_TRIBBLES,TEST_FORGROUND_BORDER_AND_LOGO,'--output='+TEST_OUTPUT])

if __name__ == "__main__":
    unittest.main()
