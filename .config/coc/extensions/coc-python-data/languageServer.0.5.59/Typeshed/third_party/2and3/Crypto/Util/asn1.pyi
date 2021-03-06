from typing import Any, Optional

class DerObject:
    typeTags = ...  # type: Any
    typeTag = ...  # type: Any
    payload = ...  # type: Any
    def __init__(self, ASN1Type: Optional[Any] = ..., payload: Any = ...) -> None: ...
    def isType(self, ASN1Type): ...
    def encode(self): ...
    def decode(self, derEle, noLeftOvers: int = ...): ...

class DerInteger(DerObject):
    value = ...  # type: Any
    def __init__(self, value: int = ...) -> None: ...
    payload = ...  # type: Any
    def encode(self): ...
    def decode(self, derEle, noLeftOvers: int = ...): ...

class DerSequence(DerObject):
    def __init__(self, startSeq: Optional[Any] = ...) -> None: ...
    def __delitem__(self, n): ...
    def __getitem__(self, n): ...
    def __setitem__(self, key, value): ...
    def __setslice__(self, i, j, sequence): ...
    def __delslice__(self, i, j): ...
    def __getslice__(self, i, j): ...
    def __len__(self): ...
    def append(self, item): ...
    def hasInts(self): ...
    def hasOnlyInts(self): ...
    payload = ...  # type: Any
    def encode(self): ...
    def decode(self, derEle, noLeftOvers: int = ...): ...

class DerOctetString(DerObject):
    payload = ...  # type: Any
    def __init__(self, value: Any = ...) -> None: ...
    def decode(self, derEle, noLeftOvers: int = ...): ...

class DerNull(DerObject):
    def __init__(self) -> None: ...

class DerObjectId(DerObject):
    def __init__(self) -> None: ...
    def decode(self, derEle, noLeftOvers: int = ...): ...
