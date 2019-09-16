import sys
import os
import shutil
import subprocess


if __name__ == '__main__':
    is64bit = sys.maxsize > 2**32

    #Run pyinstaller
    subprocess.run(["pyinstaller", "unitypackage_extractor/extractor.py",
        "--exclude-module", "ssl",
        "--exclude-module", "socket"])

    #Zip it all up
    shutil.make_archive(f"unitypackage_extractor_{'64' if is64bit else '32'}", "zip", "dist/extractor")