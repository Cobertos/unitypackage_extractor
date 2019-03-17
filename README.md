# Unity Package Extractor

Extract your .unitypackage

### Usage

* Clone down the repository
* Run `python unityPackageExtract.py [XXX.unitypackage]` and it will extract it into the current folder

#### Releasing
Refer to [the python docs on packaging for clarification](https://packaging.python.org/tutorials/packaging-projects/).
Make sure you've updated `setup.py`, and have installed `twine`, `setuptools`, and `wheel`
`python3 setup.py sdist bdist_wheel` - Create a source distribution and a binary wheel distribution into `dist/`
`twine upload dist/bobskater-x.x.x*` - Upload all `dist/` files to PyPI of a given version
Make sure to tag the commit you released