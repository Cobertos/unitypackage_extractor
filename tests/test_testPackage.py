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

    def test_packageExtractWithLeadingDots(self):
        '''should be able to extract a unity package that contains ./ in every path in the tar'''
        #arrange
        with tempfile.TemporaryDirectory() as tmp:
            #testLeadingDots.unitypackage - Same as test.unitypackage but archived with `tar -zrf archive.unitypackage .`
            #to get the specific `./` before every path

            #act
            print(f"Extracting to {tmp}...")
            extractPackage("./tests/testLeadingDots.unitypackage", outputPath=tmp)

            #assert
            self.assertTrue(os.path.isdir(tmp))
            self.assertTrue(os.path.isdir(f"{tmp}/Assets"))
            self.assertTrue(os.path.isfile(f"{tmp}/Assets/test.txt"))
            self.assertEqual(open(f"{tmp}/Assets/test.txt").read(), "testing")

    def test_packageExtractWithUnicodePath(self):
        '''should be able to extract a unity package that has a unicode pathname'''
        #arrange
        with tempfile.TemporaryDirectory() as tmp:
            # testo.unitypackage - Should just contain one file at Assets/テスト.txt with
            # contents 'testing, but with katakana!'

            #act
            print(f"Extracting to {tmp}...")
            extractPackage("./tests/testo.unitypackage", outputPath=tmp)

            #assert
            self.assertTrue(os.path.isdir(tmp))
            self.assertTrue(os.path.isdir(f"{tmp}/Assets"))
            self.assertTrue(os.path.isfile(f"{tmp}/Assets/テスト.txt"))
            self.assertEqual(open(f"{tmp}/Assets/テスト.txt").read(), "テスト, but with katakana!")