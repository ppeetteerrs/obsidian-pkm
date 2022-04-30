[Reference](https://towardsdatascience.com/byte-string-unicode-string-raw-string-a-guide-to-all-strings-in-python-684c4c4960ba)

## EUREKA Moment
Many people scratches their head when trying to comprehend string encodings because they cannot separate between the following:

| Human-readable Character | Computer Memory  | Programming Language   |
| ------------------------ | ---------------- | ---------------------- |
| ä                        | `\xc3a4c280c280` | `"\u00e4\u0080\u0080"` |

**Human-readable Characters**
The characters that you see on screen. These are displayed to you by the GPU using individual pixels in the screen.

**Computer Memory**
The character, when stored on the computer (e.g. if you save a file with the `ä` character inside it), gets saved in bytes according to the chosen encoding. Most text editors use UTF-8.

*Note: above example uses UTF-8 and Big Endian*

**Programming Language**
Your specific programming language would have a syntax for specifying Unicode strings. In Python 3, all strings are unicode by default (so `'\u0041'` and `u'\u0041'` are exactly the same). It is however important to distinguish how characters are stored in the **file** versus in **runtime and compile-time**.

For example, imagine you have following Python script (`simple.py`):
```python
v = "\u00e4\u0080\u0080"
```

Then, `simple.py` will be stored in the filesystem using the UTF-8 encoding. The characters "\", "u", "0", "0", "e", "4", ... will be stored as-in (i.e. `0x5c75303065345c75303038305c7530303830`). If you run `file simple.py`, it tells you that the document is ASCII text because the `"\u"` syntax is only used and interpreted during the Python run time.

However, during runtime, the hex value of v is set to `0xc3a4c280c280` because the python interpreter reads the string `"\u0041"` and turns it into UTF-8 bytes. But actually, you can also just do `v = "ä"`.

Also, note that some programming languages store strings as UTF-16 by default, e.g. Java.

[Unicode Converter](https://www.branah.com/unicode-converter)

## Unicode
**ASCII**
- English letters, digits and symbols stored as number between 32 and 127
- 8-bit was more than enough to store these characters

**Unicode**
- Represents every possible symbol and language
- Each character is called a code point like `U+0000` to `U+10FFFF` ([reference](http://tutorials.jenkov.com/unicode/index.html))

**UTF-8**
- One possible way to store unicode characters in bytes
- Each code point is stored using at least 1 byte and code points 0-127 (i.e. ASCII characters) store as-in. Hence backwards-compatible with ASCII
- When a byte starts with `1` (i.e., above 127), special treatment is done ([reference](https://www.johndcook.com/blog/2019/09/09/how-utf-8-works/))
- Control characters (e.g. newline, language specifiers etc.) which are not naturally displayed also exist

**UTF-16 and UTF-32**
- Minimum byte size differs

## Python Strings
As mentioned above, Python 3 strings are unicode by default so the backslash `\` has special meanings to signify special characters (e.g. `\s`, `\x`, `\u`, `\n`, `\t`, etc.). To store a backslash in a strin variable, you need to repeat every backslash (i.e. `v = "\\\\"` stores `0x5c5c` to `v`).

### Raw String
To avoid treating the backslash chracter specially and avoid going down the backslash rabbit hole, you can use raw strings `v = r"\s"` will store `0x5c73` to `v` instead of `0x20`. This is especially useful in RegEx expressions.

### Byte String / Literal
You might also have seen the syntax `b'\x41'` or `b'\u0041'`. These are byte literals which represents a byte array using strings according to the [PEP standard syntax](https://www.python.org/dev/peps/pep-3112/). The return value is of type `byte` instead of `str`.

## The Terminal
Have you also ever wondered how does Python know what encoding to use when printing strings to the terminal? As we all know, the Linux kernel only allows new processes to be created by spawning or forking from an existing process. Hence, the python process will be a child of the terminal process and environment variables are inherited. The Python interpreter can figure out the desired encoding using `$LANG` ot `$LC_CTYPE` . 

**Environment Variables**
Environment variables are stored in a virtual file `/proc/pid/environ` ([reference](https://stackoverflow.com/questions/532155/linux-where-are-environment-variables-stored)). But it can also be set and retrieved via the kernel (e.g. [putenv](https://man7.org/linux/man-pages/man3/putenv.3.html)).



