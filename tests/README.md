# Test files

### `test.unitypackage`

Expected output of package:

* `Assets/test.txt` - contents "testing"

### `testLeadingDots.unitypackage`

This one is slightly different in that the tar entries have leading `./` in the entries

Expected output of package:

* `Assets/test.txt` - contents "testing"

### `testo.unitypackage`

This one has unicode in one of the path names

Expected output of package:

* `Assets/テスト.txt` - contents "テスト, but with katakana!"