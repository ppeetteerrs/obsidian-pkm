- [TypeGuards](https://www.python.org/dev/peps/pep-0647/)
- ParamSpec
- Covariant invariant countervariant
- Annotated
- Final
- ClassVar
- Protocol
- runtime_checkable
- NamedTuple
- TypedDict
- FrozenSet
- DefaultDict
- collections
- abc
- async
- overload, cast, final
- no_type_check, type_check_only
- https://dev.to/meseta/factories-abstract-base-classes-and-python-s-new-protocols-structural-subtyping-20bm
- https://www.geeksforgeeks.org/__subclasscheck__-and-__subclasshook__-in-python/
- GenericAlias: a parameterized generics
- https://blog.daftcode.pl/covariance-contravariance-and-invariance-the-ultimate-python-guide-8fabc0c24278

- functools
classmethod => property => cache (lazy initialization)

property => abstractmethod
 
- `__get__`, `__class_getitem__` etc.
- .pyi only works when imported (makes sense, since its a stubby stub)

### Trick to Type Hint Pytorch `__call__`

```python
from typing import Callable, Literal, TypeVar, Union, cast, overload

  

from torch.nn import Module

  

C = TypeVar("C", bound=Callable)

  
  

def proxy(f: C) -> C:

 return cast(C, lambda self, *x, **y: super(self.__class__, self).__call__(*x, **y))

  
  

class M(Module):

 @overload

 def forward(self, hi: int, add: Literal[False]) -> float:

 ...

  

 @overload

 def forward(self, hi: int, add: Literal[True]) -> int:

 ...

  

 def forward(self, hi: int, add: bool) -> Union[float, int]:

 return hi + 1

  

 def another(self, nononno: str) -> None:

 print(nononno)

  

 __call__ = proxy(forward)

  
  

h = M()

h()
```