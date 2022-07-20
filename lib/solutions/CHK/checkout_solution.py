from collections import Counter
from types import DynamicClassAttribute
from typing import Dict, Iterable, Union
from itertools import chain
from lib.solutions.CHK.models import DynamicMultiPrice

from solutions.CHK.models import Freebie, Item, MultiPrice
from solutions.CHK.supermarket import FREEBIES, ITEM_CATALOG, MULTIPRICE_GROUPS


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


def sku_counter_divide(sku_counter: Dict[str, int], itemdict: Dict[str, int]) -> int:
    return min(sku_counter[sku] // qty for sku, qty in itemdict.items())

def get_multiprice_matched_items(sku_counter: Dict[str, int], multiprice: Union[MultiPrice, DynamicMultiPrice]) -> Dict[str, int]:
    if isinstance(multiprice, DynamicMultiPrice):
        return multiprice.items(sku_counter)
    if sku_counter_contains(sku_counter, multiprice.items):
        return multiprice.items
    return {}

def find_eligible_multiprices_from_group(
    sku_counter: Dict[str, int], multiprice_group: Iterable[MultiPrice]
) -> Iterable[MultiPrice]:
    eligible = []
    updated_skus_counter = sku_counter
    for multiprice in multiprice_group:
        matched_items = get_multiprice_matched_items(sku_counter, multiprice)
        while matched_items:
            eligible.append(MultiPrice(items=matched_items, price=multiprice.price))
            updated_skus_counter = sku_counter_remove(
                updated_skus_counter, matched_items
            )
            matched_items = get_multiprice_matched_items(updated_skus_counter, multiprice)
    return eligible


def find_eligible_multiprices(
    sku_counter: Dict[str, int], multiprice_groups: Iterable[Iterable[MultiPrice]]
) -> Iterable[MultiPrice]:
    return list(
        chain.from_iterable(
            find_eligible_multiprices_from_group(sku_counter, multiprice_group)
            for multiprice_group in multiprice_groups
        )
    )


def find_eligible_freebies(
    sku_counter: Dict[str, int], freebies: Iterable[Freebie]
) -> Iterable[Freebie]:
    return list(
        chain.from_iterable(
            [freebie] * sku_counter_divide(sku_counter, freebie.items)
            for freebie in freebies
            if sku_counter_contains(sku_counter, freebie.items)
        )
    )


def apply_freebies(
    sku_counter: Dict[str, int], freebies: Iterable[Freebie]
) -> Dict[str, int]:
    updated_skus_counter = sku_counter
    for freebie in freebies:
        updated_skus_counter = sku_counter_remove(
            updated_skus_counter, freebie.freebies
        )
    return updated_skus_counter


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
    if not is_valid_skus(skus, valid_skus=ITEM_CATALOG.keys()):
        return -1

    sku_counter = Counter(skus)
    print(sku_counter)

    eligible_freebies = find_eligible_freebies(sku_counter, FREEBIES)
    print(eligible_freebies)
    sku_counter = apply_freebies(sku_counter, eligible_freebies)

    eligible_multiprices = find_eligible_multiprices(sku_counter, MULTIPRICE_GROUPS)
    print(eligible_multiprices)

    print(sku_counter)
    return get_skus_total_cost(sku_counter, eligible_multiprices, ITEM_CATALOG)


