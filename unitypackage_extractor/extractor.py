import tarfile
import re
import sys
import os

def extractPackage(packagePath, outputPath=""):
  """
  Extracts a .unitypackage into the current directory
  @param {string} packagePath The path to the .unitypackage
  @param {string} [outputPath=""] Optional output path, otherwise will use cwd
  """
  with tarfile.open(name=packagePath) as upkg:
    for name in upkg.getnames():
      if re.search(r"[/\\]", name): #Only the top level files of the tar
        continue

      try:
        upkg.getmember(f"{name}/pathname")
        upkg.getmember(f"{name}/asset")
      except KeyError:
        continue #Doesn't have the required files to extract it

      #Extract the path name of the asset
      pathname = upkg.extractfile(f"{name}/pathname").readline() #Reads the first line of the pathname file
      pathname = pathname[:-1].decode("utf-8") #Remove the newling, and decode
      #Extract to the pathname
      print(f"Extracting '{name}' as '{pathname}'")
      assetFile = upkg.extractfile(f"{name}/asset")
      assetOutPath = os.path.join(outputPath, pathname)
      os.makedirs(os.path.dirname(assetOutPath), exist_ok=True) #Make the dirs up to the given folder
      open(assetOutPath, "wb").write(assetFile.read())          #Write out to our own named folder

if __name__ == "__main__":
  if not len(sys.argv) > 1:
    raise TypeError("No .unitypackage path was given. \n\nUSAGE: unitypackage_extractor [XXX.unitypackage]")
  extractPackage(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "")