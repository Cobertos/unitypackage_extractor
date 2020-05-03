import tarfile
import sys
import os
import time
import shutil 
from os import walk

def extractPackage(packagePath, outputPath=""):
  """
  Extracts a .unitypackage into the current directory
  @param {string} packagePath The path to the .unitypackage
  @param {string} [outputPath=""] Optional output path, otherwise will use cwd
  """

  # Step 1: untar all files in a temp folder
  tmpOutputPath = f"{outputPath}__TEMP__"
  tf = tarfile.open(name=packagePath)
  tf.extractall(tmpOutputPath)

  # Step 2: Extract each asset
  for dirName, subdirList, fileList in os.walk(tmpOutputPath):
    extractFile(dirName, tmpOutputPath, outputPath)

  # Step 3: Remove temp folder
  shutil.rmtree(tmpOutputPath)


def extractFile(dirName, tmpOutputPath, outputPath):
  # print('Found directory: %s' % dirName)
  if dirName == tmpOutputPath:
    return

  if not os.path.exists(f"{dirName}/pathname"):
    # print(f"*** Did not find {dirName}/pathname - Skip!")
    return
  if not os.path.exists(f"{dirName}/asset"):
    # print(f"*** Did not find {dirName}/pathname - Skip!")
    return
  with open(f"{dirName}/pathname") as f:
    pathname = f.readline()
    pathname = pathname[:-1] if pathname[-1] == '\n' else pathname #Remove newline
    assetOutPath = os.path.join(outputPath, pathname)
    os.makedirs(os.path.dirname(assetOutPath), exist_ok=True) #Make the dirs up to the given folder
    shutil.move(f"{dirName}/asset", assetOutPath)
    print(f"Extracted '{dirName}' as '{pathname}'")
    return


if __name__ == "__main__":
  if not len(sys.argv) > 1:
    raise TypeError("No .unitypackage path was given. \n\nUSAGE: unitypackage_extractor [XXX.unitypackage]")
  start_time = time.time()
  extractPackage(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "")
  print("--- Finished in %s seconds ---" % (time.time() - start_time))
