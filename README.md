<p align="center">
    <a href="https://travis-ci.org/Cobertos/unitypackage_extractor" target="_blank"><img alt="build status" src="https://travis-ci.org/Cobertos/unitypackage_extractor.svg?branch=master"></a>
    <a href="https://pypi.org/project/unitypackage_extractor/" target="_blank"><img alt="pypi python versions" src="https://img.shields.io/pypi/pyversions/unitypackage_extractor.svg"></a>
    <a href="https://twitter.com/cobertos" target="_blank"><img alt="twitter" src="https://img.shields.io/badge/twitter-%40cobertos-0084b4.svg"></a>
    <a href="https://cobertos.com" target="_blank"><img alt="twitter" src="https://img.shields.io/badge/website-cobertos.com-888888.svg"></a>
</p>

# Unity Package Extractor


Extract your .unitypackage

### Usage without Python

* Download the [unitypackage_extractor.zip](https://github.com/Cobertos/unitypackage_extractor/releases/tag/0.3.0) from the Releases tab.
* Extract everything into a new directory
* Run the `extractor.exe` inside with `extractor.exe [path/to/your/package.unitypackage] (optional/output/path)`

### Usage with Python 3.6+

* `pip install unitypackage_extractor`

* From the command line `python -m unitypackage_extractor.extractor [path/to/your/package.unitypackage] (optional/output/path)`

* OR in your Python file:
```python
from unitypackage_extractor.extractor import extractPackage

extractPackage("path/to/your/package.unitypackage", outputPath="optional/output/path")
```

### Contributing
#### Building
Install `pyinstaller` and run `build_exe.py`. I couldn't get this to work with Python 3.7 so I downloaded and ran it with 3.6 and it worked.

#### Testing
Install `pytest` and run `pytest -v -s` in the root directory.

#### Releasing
Refer to [the python docs on packaging for clarification](https://packaging.python.org/tutorials/packaging-projects/).
Make sure you've updated `setup.py`, and have installed `twine`, `setuptools`, and `wheel`
`python3 setup.py sdist bdist_wheel` - Create a source distribution and a binary wheel distribution into `dist/`
`twine upload dist/unitypackage_extractor-x.x.x*` - Upload all `dist/` files to PyPI of a given version
Make sure to tag the commit you released