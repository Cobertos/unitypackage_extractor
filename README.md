# Unity Package Extractor

Extract your .unitypackage

### Usage without Python

* TODO:
* Run `python unityPackageExtract.py [XXX.unitypackage]` and it will extract it into the current folder

### Usage with Python

* `pip install unitypackage_extractor`

* From the command line `python -m unitypackage_extractor.extractor [XXX.unitypackage]`

* OR in your Python file:
```python
from unitypackage_extractor.extractor import extractPackage

extractPackage("path/to/your/package")
```

### Contributing
#### Releasing
Refer to [the python docs on packaging for clarification](https://packaging.python.org/tutorials/packaging-projects/).
Make sure you've updated `setup.py`, and have installed `twine`, `setuptools`, and `wheel`
`python3 setup.py sdist bdist_wheel` - Create a source distribution and a binary wheel distribution into `dist/`
`twine upload dist/unitypackage_extractor-x.x.x*` - Upload all `dist/` files to PyPI of a given version
Make sure to tag the commit you released