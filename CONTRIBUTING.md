# Contributing

Here's how to run all the development stuff.

## Setup Development Environment
* `pyenv global 3.7.6-amd64`
* `pipenv install --dev`

## Building

Building is a little convoluted because we build a x64 and an x86 binary, because we don't have it in the Pipfile because it didn't play nicely with CI the last time I tried, and `pipenv` doesn't play nicely with bitness.

If this project accumulates and Pipfile dependencies that `pyinstaller` needs to know about, we either have to stop using `pipenv` or find a new way to manage this...

EDIT: `pipenv` is apparently dead? No new releases? So... don't use it to build with for now...

* `pyenv global 3.7.6-amd64`
* `pipenv run pip freeze > tmp-requirements.txt`
* `pip install -r tmp-requirements.txt`
* `pip install pyinstaller`
 * pyinstaller is a slower dependency so might not work with the latest Python
* `python build_exe.py`
* Do the same with `pyenv global 3.7.6` (without `-amd64` suffix) to build the x86 .exe

## Testing
* `pipenv run pytest -v` in the root directory

## Releasing
Refer to [the python docs on packaging for clarification](https://packaging.python.org/tutorials/packaging-projects/).
* Make sure you've updated `setup.py`
* `python setup.py sdist bdist_wheel` - Create a source distribution and a binary wheel distribution into `dist/`
* `twine upload dist/unitypackage_extractor-x.x.x*` - Upload all `dist/` files to PyPI of a given version
* Make sure to tag the commit you released!