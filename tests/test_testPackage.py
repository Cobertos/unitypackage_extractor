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
    with tempfile.TemporaryDirectory() as tmp2:
      #test.unitypackage - Should contain one file named test.txt with the contents "testing"
      extractPath = os.path.abspath("./tests/test.unitypackage")

      # change directory due to Windows failing when relative paths are on different
      # drives (so use _two_ temp folders)
      oldDir = os.path.abspath('.')
      relTmp = os.path.relpath(tmp, start=tmp2)
      os.chdir(tmp2)

      #act
      print(f"Extracting to {tmp} as {relTmp}...")
      extractPackage(extractPath, outputPath=relTmp)
      os.chdir(oldDir)

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

def test_packageExtractBadWindowsCharacters():
  '''should be able to extract a package even if theres reserved Windows characters'''
  #arrange
  with tempfile.TemporaryDirectory() as tmp:
    #testBadWinChars.unitypackage - One file named "*:?gotem.txt", contents "testing"

    #act
    print(f"Extracting to {tmp}...")
    extractPackage("./tests/testBadWinChars.unitypackage", outputPath=tmp)

    #assert
    assert os.path.isdir(tmp)
    assert os.path.isdir(f"{tmp}/Assets")
    correctName = '___gotem.txt' if os.name == 'nt' else '*:?gotem.txt'
    assert os.path.isfile(f"{tmp}/Assets/{correctName}")
    assert open(f"{tmp}/Assets/{correctName}").read() == "testing"

def test_packageExtractCWD():
  '''should be able to extract a simple unity pckage to cwd (no output path)'''
  #arrange
  with tempfile.TemporaryDirectory() as tmp:
    #test.unitypackage - Should contain one file named test.txt with the contents "testing"
    extractPath = os.path.abspath("./tests/test.unitypackage")
    oldCwd = os.getcwd()
    os.chdir(tmp) # Switch to the path we'll extract to

    #act
    print(f"Extracting to cwd, '{os.getcwd()}'...")
    extractPackage(extractPath)
    os.chdir(oldCwd) # Go back to old path

    #assert
    assert os.path.isdir(f"{tmp}/Assets")
    assert os.path.isfile(f"{tmp}/Assets/test.txt")
    assert open(f"{tmp}/Assets/test.txt").read() == "testing"
