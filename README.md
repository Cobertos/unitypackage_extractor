<p align="center">
    <a href="https://github.com/Cobertos/unitypackage_extractor/actions" target="_blank"><img alt="build status" src="https://github.com/Cobertos/unitypackage_extractor/workflows/Package%20Tests/badge.svg"></a>
    <a href="https://pypi.org/project/unitypackage_extractor/" target="_blank"><img alt="pypi python versions" src="https://img.shields.io/pypi/pyversions/unitypackage_extractor.svg"></a>
    <a href="https://twitter.com/cobertos" target="_blank"><img alt="twitter" src="https://img.shields.io/badge/twitter-%40cobertos-0084b4.svg"></a>
    <a href="https://cobertos.com" target="_blank"><img alt="twitter" src="https://img.shields.io/badge/website-cobertos.com-888888.svg"></a>
    <a href="https://tidelift.com/subscription/pkg/pypi-unitypackage-extractor?utm_source=pypi-unitypackage-extractor&utm_medium=referral&utm_campaign=readme" target="_blank"><img alt="Tidelift - For Enterprise" src="https://img.shields.io/static/v1?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAMCAYAAABSgIzaAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAACjSURBVChTrZAxDoJAEEV3oNGCQk6ihYXH8hhehmt4DCoaGwsrE+L4f/LByboQC1/ymM2fmYRdc/chpbSDOSfVq2rkXuHTwG1Bk6Vew8UWboL8gxxmcaatzGyEz0mEDslLEo8zcFT+AXfu4RnyTHnu1V4GQwdVPhzvOGerYKiGF7iXPNdqL4OhDpJpkXRqz/BVc46qka+stPgTf128wUcms0BKbwwmZGRFmSUVAAAAAElFTkSuQmCC&message=For%20Enterprise&color=F6914D&label=%7F"></a>
</p>

# Unity Package Extractor

Extract your .unitypackage

## Usage without Python

* Download the [unitypackage_extractor.zip](https://github.com/Cobertos/unitypackage_extractor/releases/latest) from the Releases tab.
* Extract into a new directory
* Drag and drop your `.unitypackage` onto `extractor.exe` OR
* Run from the command line with `extractor.exe [path/to/your/package.unitypackage] (optional/output/path)`

## Usage with Python 3.6+

* `pip install unitypackage_extractor`

* From the command line `python -m unitypackage_extractor [path/to/your/package.unitypackage] (optional/output/path)`

* OR in your Python file:
```python
from unitypackage_extractor.extractor import extractPackage

extractPackage("path/to/your/package.unitypackage", outputPath="optional/output/path")
```

## For Enterprise

The maintainers of thousands of packages (including me! :3) are working with Tidelift to deliver commercial support and maintenance for the open source dependencies you use to build your applications. Save time, reduce risk, and improve code health, while paying the maintainers of the exact dependencies you use. [Learn more.](https://tidelift.com/subscription/pkg/pypi-unitypackage-extractor?utm_source=pypi-unitypackage-extractor&utm_medium=referral&utm_campaign=readme)

## Contributing
See [CONTRIBUTING.md](https://github.com/Cobertos/md2notion/blob/master/CONTRIBUTING.md)