import tarfile
import tempfile
import sys
import os
import time
import shutil

def extractPackage(packagePath, outputPath="", encoding='utf-8'):
  """
  Extracts a .unitypackage into the current directory
  @param {string} packagePath The path to the .unitypackage
  @param {string} [outputPath=""] Optional output path, otherwise will use cwd
  """
  with tempfile.TemporaryDirectory() as tmpDir:
    # Unpack the whole thing in one go (faster than traversing the tar)
    with tarfile.open(name=packagePath, encoding=encoding) as upkg:
      upkg.extractall(tmpDir)

    # Extract each file in tmpDir to final destination
    for dirEntry in os.scandir(tmpDir):
      assetEntryDir = f"{tmpDir}/{dirEntry.name}"
      if not os.path.exists(f"{assetEntryDir}/pathname") or \
          not os.path.exists(f"{assetEntryDir}/asset"):
        continue #Doesn't have the required files to extract it

      # Has the required info to extract
      # Get the path to output to from /pathname
      with open(f"{assetEntryDir}/pathname", encoding=encoding) as f:
        pathname = f.readline()
        pathname = pathname[:-1] if pathname[-1] == '\n' else pathname #Remove newline

      #Extract to the pathname
      print(f"Extracting '{dirEntry.name}' as '{pathname}'")
      assetOutPath = os.path.join(outputPath, pathname)
      os.makedirs(os.path.dirname(assetOutPath), exist_ok=True) #Make the dirs up to the given folder
      shutil.move(f"{assetEntryDir}/asset", assetOutPath)

def cli(args):
  if not args:
    raise TypeError("No .unitypackage path was given. \n\nUSAGE: unitypackage_extractor [XXX.unitypackage]")
  startTime = time.time()
  extractPackage(args[0], args[1] if len(args) > 1 else "")
  print("--- Finished in %s seconds ---" % (time.time() - startTime))

if __name__ == "__main__":
  cli(sys.argv[1:])