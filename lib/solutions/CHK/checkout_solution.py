
from dataclasses import dataclass

@dataclass
class Item:
    name: str
    price: int

ITEMS = {
    "A": Item(name="A", price=50),
    "B": Item(name="B", price=30),
    "C": Item(name="C", price=20),
    "D": Item(name="D", price=15)
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    print(ITEMS)

