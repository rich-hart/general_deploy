import os
from os.path import dirname, realpath, join, basename
import unittest
import argparse
import json
import numpy
import cv2
import cv
import subprocess

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
    parser.add_argument('fan_picture', type=argparse.FileType('rb'))
    parser.add_argument('--output', type=argparse.FileType('wb+'))
    args = parser.parse_args(argv)
    settings = vars(args)
    if not settings['output']:
        settings['output'] = join(dirname(settings['fan_picture'].name),'tribified_'+basename(settings['fan_picture'].name))
    command = "python merge_layers.py {0} {1} {2} {3} {4} --output={5}".format(
        BACKGROUND_WALL,
        BACKGROUND_TRIBBLES,
        settings['fan_picture'].name,
        FORGROUND_TRIBBLES,
        FORGROUND_BORDER_AND_LOGO,
        settings['output'],
    )
    subprocess.call(command.split(' '))
    return settings



TEST_DIR = join(dirname(realpath(__file__)),'tests')
TEST_DATA = os.path.join(TEST_DIR,'data')
TEST_CAPTAIN = os.path.join(TEST_DATA, 'captain.png')

class TestTribbify(unittest.TestCase):
    def setUp(self):
        self.captain_img = cv2.imread(TEST_CAPTAIN)
        self.blue, self.green, self.red = cv2.split(self.captain_img)
 
    def test(self):
        pass

    def test_main(self):
        main([FAN_PICTURE])

if __name__ == "__main__":
    unittest.main()
