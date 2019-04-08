'''
Tests for package extracting
'''
import os
import unittest
import tempfile

from unitypackage_extractor.extractor import extractPackage

class TestTestPackageExtract(unittest.TestCase):
    '''
    Tests the package extracting functionality
    '''
    def test_packageExtract(self):
        '''should be able to extract a simple unity pckage'''
        #arrange
        with tempfile.TemporaryDirectory() as tmp:
            #test.unitypackage - Should contain one file named test.txt with the contents "testing"

            #act
            print(f"Extracting to {tmp}...")
            extractPackage("./tests/test.unitypackage", outputPath=tmp)

            #assert
            self.assertTrue(os.path.isdir(tmp))
            self.assertTrue(os.path.isdir(f"{tmp}/Assets"))
            self.assertTrue(os.path.isfile(f"{tmp}/Assets/test.txt"))
            self.assertEqual(open(f"{tmp}/Assets/test.txt").read(), "testing")