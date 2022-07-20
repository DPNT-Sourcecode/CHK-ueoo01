from typing import Dict, Iterable


def any_n_of_items(n: int, skuset: Iterable[str], sku_counter: Dict[str, int]) -> Dict[str, int]:
    total, matched = 0, {}
    for sku in skuset:
        if sku in sku_counter:
            matched[sku] = sku_counter[sku] if total + sku_counter[sku] <= n else n - total
    
        if total >= n:
            print(matched)
            return matched
    return {}
            

