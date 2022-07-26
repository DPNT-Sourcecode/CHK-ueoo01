from functools import partial
import string

from solutions.CHK.matchers import any_n_of_items
from solutions.CHK.models import DynamicMultiPrice
from solutions.CHK.models import Freebie, Item, MultiPrice

prices = [50, 30, 20, 15, 40, 10 ,20, 10, 35, 60, 70, 90, 15, 40, 10, 50, 30, 50, 20, 20, 40, 50, 20, 17, 20, 21]

ITEM_CATALOG = {
    sku: Item(name=sku, price=price) for sku, price in zip(string.ascii_uppercase, prices)
}


# order in multiprice group defines precedence
MULTIPRICE_GROUPS = [
    [MultiPrice(items={"A": 5}, price=200), MultiPrice(items={"A": 3}, price=130)],
    [MultiPrice(items={"B": 2}, price=45)],
    [MultiPrice(items={"H": 10}, price=80), MultiPrice(items={"H": 5}, price=45)],
    [MultiPrice(items={"K": 2}, price=120)],
    [MultiPrice(items={"P": 5}, price=200)],
    [MultiPrice(items={"Q": 3}, price=80)],
    [MultiPrice(items={"V": 3}, price=130), MultiPrice(items={"V": 2}, price=90)],
    [
        DynamicMultiPrice(
            items=partial(any_n_of_items, 3, ("Z", "S", "T", "Y", "X")),
            price=45
        )
    ]
]

FREEBIES = [
    Freebie(items={"E": 2, "B": 1}, freebies={"B": 1}),
    Freebie(items={"F": 3}, freebies={"F": 1}),
    Freebie(items={"N": 3, "M": 1}, freebies={"M": 1}),
    Freebie(items={"R": 3, "Q": 1}, freebies={"Q": 1}),
    Freebie(items={"U": 4}, freebies={"U": 1}),
]

