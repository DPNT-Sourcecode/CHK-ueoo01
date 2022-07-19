from collections import Counter
from dataclasses import dataclass
from typing import Dict, Iterable
from itertools import chain


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
    "D": Item(name="D", price=15),
    "E": Item(name="E", price=40),
}

# order in multiprice group defines precedence
MULTIPRICE_GROUPS = [
    [MultiPrice(items={"A": 5}, price=200), MultiPrice(items={"A": 3}, price=130)]
    [MultiPrice(items={"B": 2}, price=45)],
]


def is_valid_skus(skus: str, valid_skus: Iterable[str]) -> bool:
    return all(sku in valid_skus for sku in skus)


def sku_counter_contains(sku_counter: Dict[str, int], itemdict: Dict[str, int]) -> bool:
    return all(
        sku in sku_counter and qty <= sku_counter[sku] for sku, qty in itemdict.items()
    )


def sku_counter_remove(
    sku_counter: Dict[str, int], itermdict: Dict[str, int]
) -> Dict[str, int]:
    new_sku_counter = sku_counter.copy()
    for sku, qty in itermdict.items():
        new_sku_counter[sku] -= qty
        if new_sku_counter[sku] == 0:
            del new_sku_counter[sku]
    return new_sku_counter


def multiprice_multiplier(sku_counter: Dict[str, int], multiprice: MultiPrice) -> int:
    return min(sku_counter[sku] // qty for sku, qty in multiprice.items.items())


def find_eligible_multiprices(
    sku_counter: Dict[str, int], multiprice_groups: Iterable[Iterable[MultiPrice]]
) -> Iterable[MultiPrice]:
    return list(
        chain.from_iterable(
            [multiprice] * multiprice_multiplier(sku_counter, multiprice)
            for multiprice in multiprices
            if sku_counter_contains(sku_counter, multiprice.items)
        )
    )


def get_skus_total_cost(
    sku_counter: Dict[str, int],
    eligible_multiprices: Iterable[MultiPrice],
    item_catalog: Dict[str, Item],
) -> int:
    total_cost = 0

    updated_sku_counter = sku_counter
    for multiprice in eligible_multiprices:
        total_cost += multiprice.price
        updated_sku_counter = sku_counter_remove(updated_sku_counter, multiprice.items)

    for sku, qty in updated_sku_counter.items():
        total_cost += item_catalog[sku].price * qty

    return total_cost


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    if not is_valid_skus(skus, valid_skus=ITEMS.keys()):
        return -1

    sku_counter = Counter(skus)
    print(sku_counter)
    eligible_multiprices = find_eligible_multiprices(sku_counter, MULTIPRICES)
    print(eligible_multiprices)
    return get_skus_total_cost(sku_counter, eligible_multiprices, ITEMS)

