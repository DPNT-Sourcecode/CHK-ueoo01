

from lib.solutions.CHK.models import Freebie, Item, MultiPrice


ITEM_CATALOG = {
    "A": Item(name="A", price=50),
    "B": Item(name="B", price=30),
    "C": Item(name="C", price=20),
    "D": Item(name="D", price=15),
    "E": Item(name="E", price=40),
    "F": Item(name="F", price=10),
}

# order in multiprice group defines precedence
MULTIPRICE_GROUPS = [
    [MultiPrice(items={"A": 5}, price=200), MultiPrice(items={"A": 3}, price=130)],
    [MultiPrice(items={"B": 2}, price=45)],
]

FREEBIES = [
    Freebie(items={"E": 2, "B": 1}, freebies={"B": 1}),
    Freebie(items={"F": 3}, freebies={"F": 1})
]

