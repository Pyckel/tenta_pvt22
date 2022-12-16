import requests
from typing import Optional


CATEGORIES = {"fysik": "phy",
              "kemi": "che",
              "litteratur": "lit",
              "ekonomi": "eco",
              "fred": "pea",
              "medicin": "med"}


def get_info(year: str, category: str = None) -> Optional[dict]:
    # skickar en förfrågan till api med den information som användaren angav
    if category is not None:
        if category in CATEGORIES:
            category = CATEGORIES[category]
            current_search = {"nobelPrizeYear": int(year), "nobelPrizeCategory": category}
        else:
            print('Det var ingen giltig kategori du skrev in')
            return None
    else:
        current_search = {"nobelPrizeYear": int(year)}
    result = requests.get("http://api.nobelprize.org/2.1/nobelPrizes", params=current_search).json()
    return result
