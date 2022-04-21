## Preface
Python imports has always been a confusing topic for me. The dreaded `ImportError: attempted relative import with no known parent package` has haunted me for years. And now, I have decided to figure things out once and for all. (No more fear of running a Python script not in the project root directory yay!)

## Do we still need `__init__.py`?
> [The Zen of Python](https://www.python.org/dev/peps/pep-0020/): Explicit is better than implicit.

Since Python 3.3 (please leave if you use anything older than that, you are not welcomed), `__ini__.py` is not longer a must for the Python import system. But what exactly happens with / without `__init__.py`? ([reference](http://python-notes.curiousefficiency.org/en/latest/python_concepts/import_traps.html))

### When to include `__init__.py`?
> Include `__init__.py` when you don't want to open up your namespace to third party contributions (e.g. all standard library packages).

Without `__init__.py`, multiple directories can contribute to the same package. With `__init__.py`, a single directory package is created (masking preceding, matching subdirectories on `sys.path` without `__init__.py`).

Consider the following directory layout:
```txt
project/
    example/
        foo.py
project2/
    example/
        __init__.py
        bar.py
```

We can see the expected results:
```txt
$ PYTHONPATH=../project2 python3 -c "import example.bar"
Hello from  example.bar
$ PYTHONPATH=../project2 python3 -c "import example.foo"
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ImportError: No module named 'example.foo'

$ rm ../project2/example/__init__.py
$ PYTHONPATH=../project2 python3 -c "import example.bar"
Hello from  example.bar
$ PYTHONPATH=../project2 python3 -c "import example.foo"
Hello from  example.foo
```

## With `-m` or without `m`?
I can't even count how many times I used to do `python sub_dir/script.py` and get `ImportError: attempted relative import with no known parent package`...

### What does the `-m` do?
When you run `python sub_dir/script.py`, the file is run as a **script**, meaning that the file's parent directory is added to `sys.path` at index `0`. As such, relative imports inside `sub_dir/script.py` like `from ..xxx import yyy` do not work as the parent directory of `sub_dir` is not inside `sys.path` (imagine the rabit hole that is opened if Python searches through every parent directory of `script.py` for packages hmmm).

> If this option is given, the first element of [`sys.argv`](https://docs.python.org/2/library/sys.html#sys.argv) will be the full path to the module file. As with the [`-c`](https://docs.python.org/2/using/cmdline.html#cmdoption-c) option, the current directory will be added to the start of [`sys.path`](https://docs.python.org/2/library/sys.html#sys.path). ([see]([[https://docs.python.org/2/using/cmdline.html#cmdoption-m]]))

If we run `python -m sub_dir/script`, the `sys.path` behaviour is described above. The Python interpreter will then "search `sys.path` for the named module and execute its contents as the `__main__` module". Thus, the relative imports work as expected.

### Why is `-m` not the default behaviour?
The content above would probably leave a lot of you (including me) wondering why `-m` is not the default behaviour since often times we actually want to execute a script as a module. To answer that, I would quote Martijn Pieters's answer [here](https://stackoverflow.com/questions/22241420/execution-of-python-code-with-m-option-or-not).
> Scripts can be opened in _any arbitrary path_ and then their parent directory is added to the module search path. `-m` only works for the current directory or directories already registered on the search path. That was my point. `-m` is not something you give to end-users for that very usability issue.

