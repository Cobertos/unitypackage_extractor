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

### `testEscape.unitypackage`

This one has a path with .. in it, which should cause a failure

No expected output, but contains:

* `../escape.txt`

### `testEscape2.unitypackage`

This one has an absolute path, which should cause a failure. `/tmp` because it's
globally writable on most systems.

No expected output, but contains:

* `/tmp/escape.txt`

### `testBadWinChars.unitypackage`

This one has a filename with characters Windows will dislike. The filename is `*:?gotem.txt`

Expected output of package:

* `Assets/___gotem.txt` on Windows, `Assets/*:?gotem.txt` on Linux - contents "testing"