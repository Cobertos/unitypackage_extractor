# Contributing

Here's how to run all the development stuff.

## Setup Development Environment
* `pyenv global 3.7.6-amd64` (or whatever the latest is pyinstaller supports, sometimes it's not up to date)
* `pipenv install --dev`

## Building

Building is a little convoluted because we build a x64 and an x86 binary.

TODO: not sure if `pyenv global` is still needed. In the past I think it had trouble with local versions of different python bitness

* `pyenv global 3.7.6-amd64`
* `pipenv run pip freeze > tmp-requirements.txt`
* `pip install -r tmp-requirements.txt`
* `pip install pyinstaller`
* `pyinstaller --onefile unitypackage_extractor/extractor.py` (or `python -m PyInstaller`, idk why but `pyinstaller` doesn't work sometimes)
* Do the same with `pyenv global 3.7.6` (without `-amd64` suffix) to build the x86 .exe

## Testing
* `pipenv run pytest -v` in the root directory

## Releasing
Refer to [the python docs on packaging for clarification](https://packaging.python.org/tutorials/packaging-projects/).
* Make sure you've updated `setup.py`
* `python setup.py sdist bdist_wheel` - Create a source distribution and a binary wheel distribution into `dist/`
* `twine upload dist/unitypackage_extractor-x.x.x*` - Upload all `dist/` files to PyPI of a given version
* Make sure to tag the commit you released!