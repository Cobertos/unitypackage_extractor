'''
Tests for package extracting
'''
import io
import sys
import re
import os
import tempfile

from unitypackage_extractor.extractor import extractPackage

def test_packageExtract():
  '''should be able to extract a simple unity pckage'''
  #arrange
  with tempfile.TemporaryDirectory() as tmp:
    #test.unitypackage - Should contain one file named test.txt with the contents "testing"

    #act
    print(f"Extracting to {tmp}...")
    extractPackage("./tests/test.unitypackage", outputPath=tmp)

    #assert
    assert os.path.isdir(tmp)
    assert os.path.isdir(f"{tmp}/Assets")
    assert os.path.isfile(f"{tmp}/Assets/test.txt")
    assert open(f"{tmp}/Assets/test.txt").read() == "testing"

def test_packageExtractRelative():
  '''should be able to extract to a relative path'''
  #arrange
  with tempfile.TemporaryDirectory() as tmp:
    #test.unitypackage - Should contain one file named test.txt with the contents "testing"
    relTmp = os.path.relpath(tmp, start=".")

    #act
    print(f"Extracting to {tmp} as {relTmp}...")
    extractPackage("./tests/test.unitypackage", outputPath=os.path.relpath(relTmp))

    #assert
    assert os.path.isdir(tmp)
    assert os.path.isdir(f"{tmp}/Assets")
    assert os.path.isfile(f"{tmp}/Assets/test.txt")
    assert open(f"{tmp}/Assets/test.txt").read() == "testing"

def test_packageExtractWithLeadingDots():
  '''should be able to extract a unity package that contains ./ in every path in the tar'''
  #arrange
  with tempfile.TemporaryDirectory() as tmp:
    #testLeadingDots.unitypackage - Same as test.unitypackage but archived with `tar -zrf archive.unitypackage .`
    #to get the specific `./` before every path

    #act
    print(f"Extracting to {tmp}...")
    extractPackage("./tests/testLeadingDots.unitypackage", outputPath=tmp)

    #assert
    assert os.path.isdir(tmp)
    assert os.path.isdir(f"{tmp}/Assets")
    assert os.path.isfile(f"{tmp}/Assets/test.txt")
    assert open(f"{tmp}/Assets/test.txt").read() == "testing"

def test_packageExtractWithUnicodePath():
  '''should be able to extract a unity package that has a unicode pathname'''
  #arrange
  with tempfile.TemporaryDirectory() as tmp:
    # testo.unitypackage - Should just contain one file at Assets/テスト.txt with
    # contents 'testing, but with katakana!'

    #act
    print(f"Extracting to {tmp}...")
    extractPackage("./tests/testo.unitypackage", outputPath=tmp)

    #assert
    assert os.path.isdir(tmp)
    assert os.path.isdir(f"{tmp}/Assets")
    assert os.path.isfile(f"{tmp}/Assets/テスト.txt")
    assert open(f"{tmp}/Assets/テスト.txt").read(), "テスト == but with katakana!"

def test_packageExtractEscape(capsys):
  '''should skip relative paths that are outside'''
  #arrange
  with tempfile.TemporaryDirectory() as tmp:
    # testEscape.unitypackage - Should skip relative paths

    #act
    print(f"Extracting to {tmp}...")
    extractPackage("./tests/testEscape.unitypackage", outputPath=tmp)
    out, err = capsys.readouterr()
    sys.stdout.write(out)
    sys.stderr.write(err)

    #assert
    assert os.path.isdir(tmp)
    assert not os.path.isfile(f"{tmp}/../escape.txt")
    assert re.search(r"outside", out, flags=re.IGNORECASE)

def test_packageExtractEscape2(capsys):
  '''should skip absolute paths'''
  #arrange
  with tempfile.TemporaryDirectory() as tmp:
    # testEscape2.unitypackage - Should skip absolute paths

    #act
    print(f"Extracting to {tmp}...")
    extractPackage("./tests/testEscape2.unitypackage", outputPath=tmp)
    out, err = capsys.readouterr()
    sys.stdout.write(out)
    sys.stderr.write(err)

    #assert
    assert os.path.isdir(tmp)
    assert not os.path.isfile(f"/tmp/escape.txt")
    assert re.search(r"outside", out, flags=re.IGNORECASE)
