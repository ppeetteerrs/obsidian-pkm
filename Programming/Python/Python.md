## Below the Hoods
[[Python Imports]]
[Named Tuples](http://zecong.hu/2019/08/10/inheritance-for-namedtuples/)

## Tricks
- super outside class
- lru_cache
- [module as class](https://mail.python.org/pipermail/python-ideas/2012-May/014969.html) ([also](https://stackoverflow.com/questions/2447353/getattr-on-a-module/7668273#7668273))
- muting imported library tqdm
```python
from lungmask import mask, utils

def nop(item: Any, *_: Any, **__: Any) -> Any:

"""

NOP function overload to silent imported libraries.

"""



return item

# Make lungmask tqdm quiet

mask.tqdm = nop

utils.tqdm = nop
```


## Concepts
[[Python Strings]]
[[Python RegEx]]
[[RegEx Cheatsheet]]
[[Python Advanced Typings]]
todo: python string types e.g. r'', b'', u''
Context Manager from Generator


### Python Utils
- listify, stringify, tuplify (type hint up to length 10??)
- Pytorch `__call__` type hint

Argument Parsing: https://github.com/lebrice/SimpleParsing

Inherited Dicts
https://treyhunner.com/2019/04/why-you-shouldnt-inherit-from-list-and-dict-in-python/
https://chriswarrick.com/blog/2018/09/20/python-hackery-merging-signatures-of-two-python-functions/

https://www.kaggle.com/rohanrao/tutorial-on-reading-large-datasets

https://bergvca.github.io/2017/10/14/super-fast-string-matching.html

https://www.sympy.org/scipy-2017-codegen-tutorial/notebooks/20-ordinary-differential-equations.html

https://dev.to/meseta