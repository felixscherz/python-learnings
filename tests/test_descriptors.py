from typing import Generic
from typing import TypeVar
import pytest

T = TypeVar("T")


class Validated(Generic[T]):
    def __init__(self, dtype: type[T]) -> None:
        self.dtype = dtype

    def __set_name__(self, owner, name):
        self.public = name
        self.private = "_" + name

    def __set__(self, obj, value: T):
        if not isinstance(value, self.dtype):
            raise ValueError("Wrong type")
        setattr(obj, self.private, value)

    def __get__(self, instance, owner=None) -> T:
        return getattr(instance, self.private)


class Person:
    name = Validated(str)

    def __init__(self, name) -> None:
        self.name = name

    def a(self):
        self.name


def test_person():
    with pytest.raises(ValueError):
        Person(name=0)

    assert Person(name="foo")
