from dataclasses import dataclass
from typing import Callable, Dict


@dataclass
class Item:
    name: str
    price: int


@dataclass
class MultiPrice:
    items: Dict[str, int]
    price: int


@dataclass
class DynamicMultiPrice:
    items: Callable[..., Dict[str, int]]
    price: int


@dataclass
class Freebie:
    items: Dict[str, int]
    freebies: Dict[str, int]


