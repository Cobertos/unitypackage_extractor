import os
import shutil
import subprocess

#Run pyinstaller
subprocess.run(["pyinstaller", "unitypackage_extractor/extractor.py",
    "--exclude-module", "ssl",
    "--exclude-module", "socket"])
os.remove("dist/extractor/libcrypto-1_1.dll")
os.remove("dist/extractor/base_library.zip")

#Zip it all up
shutil.make_archive("unitypackage_extractor", "zip", "dist/extractor")