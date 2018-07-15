import os
from os.path import dirname, realpath, join
import unittest
import argparse
import json
import numpy
import cv2
import cv
def main(argv=None):
    import ipdb; ipdb.set_trace()
    parser = argparse.ArgumentParser(
        description='Return a list of related pages between two pdfs.')
    parser.add_argument('input', type=argparse.FileType('r'))
    args = parser.parse_args(argv)
    settings = vars(args)
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
        main([TEST_CAPTAIN])

if __name__ == "__main__":
    unittest.main()
