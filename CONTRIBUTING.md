# Contributing

Here's how to run all the development stuff.

## Setup Development Environment
* `pyenv global 3.6.8-amd64`
* `pipenv install --dev`

## Building

Building is a little convoluted because we build a x64 and an x86 binary...

* `pyenv global 3.6.8-amd64`
 * Originally wasn't able to get this to run on Python 3.7 when it was new, but 3.6 is guarenteed to build the `.exe`
* `pyenv exec python -m venv venv64`
* `venv64\scripts\activate.bat` or `venv64/scripts/activate` for Linux
* `pip install -r requirements-dev.txt` (Installs `pyinstaller` and `pytest`)
* `python build_exe.py`
* `venv64\scripts\deactivate.bat` (or you'll use the wrong python when you make another `venv`)
* Do the same with `pyenv and 3.6.8` and make a folder called `venv32` instead

## Testing
* `pipenv run pytest -v` in the root directory

## Releasing
Refer to [the python docs on packaging for clarification](https://packaging.python.org/tutorials/packaging-projects/).
* Make sure you've updated `setup.py`
* `python setup.py sdist bdist_wheel` - Create a source distribution and a binary wheel distribution into `dist/`
* `twine upload dist/unitypackage_extractor-x.x.x*` - Upload all `dist/` files to PyPI of a given version
* Make sure to tag the commit you released!