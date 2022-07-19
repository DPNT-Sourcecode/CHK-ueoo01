
from collections import Counter
from dataclasses import dataclass
from typing import Dict, Iterable

@dataclass
class Item:
    name: str
    price: int


@dataclass
class MultiPrice:
    items: Dict[str, int] 
    price: int


ITEMS = {
    "A": Item(name="A", price=50),
    "B": Item(name="B", price=30),
    "C": Item(name="C", price=20),
    "D": Item(name="D", price=15)
}

MULTIPRICES = [
    MultiPrice(items={"A":3}, price=130),
    MultiPrice(items={"B":2}, price=45),
]

def is_valid_skus(skus: str, valid_skus: Iterable[str]) -> bool:
    return all(sku in valid_skus for sku in skus)

def sku_counter_contains(sku_counter: Dict[str, int], itemdict: Dict[str, int]) -> bool:
    return all(sku in sku_counter and qty <= sku_counter[sku] for sku, qty in itemdict.items())

def find_eligible_multiprices(sku_counter: Dict[str, int], multiprices: Iterable[MultiPrice]) -> Iterable[MultiPrice]:
    return [
        multiprice for multiprice in multiprices if sku_counter_contains(sku_counter, multiprice.items)
    ]
        

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    if not is_valid_skus(skus, valid_skus=ITEMS.keys()):
        return -1
    
    sku_counter = Counter(skus)

    print(sku_counter)

    eligible_multiprices = find_eligible_multiprices(sku_counter, MULTIPRICES)
    print(eligible_multiprices)

    # print(sku_counter_contains(sku_counter, {"A": 2}))

    return 0