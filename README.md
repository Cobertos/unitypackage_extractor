# Unity Package Extractor

Extract your .unitypackage

### Usage without Python

* Download the [unitypackage_extractor.zip](https://github.com/Cobertos/unitypackage_extractor/raw/master/unitypackage_extractor.zip)
* Extract everything into a new directory
* Run the `extractor.exe` inside with `extractor.exe [path/to/your/package.unitypackage] (optional/output/path)`

### Usage with Python

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


#### Releasing
Refer to [the python docs on packaging for clarification](https://packaging.python.org/tutorials/packaging-projects/).
Make sure you've updated `setup.py`, and have installed `twine`, `setuptools`, and `wheel`
`python3 setup.py sdist bdist_wheel` - Create a source distribution and a binary wheel distribution into `dist/`
`twine upload dist/unitypackage_extractor-x.x.x*` - Upload all `dist/` files to PyPI of a given version
Make sure to tag the commit you released