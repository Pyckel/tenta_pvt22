import requests

CATEGORIES = {"fysik": "phy",
       "kemi": "che",
       "litteratur": "lit",
       "ekonomi": "eco",
       "fred": "pea",
       "medicin": "med"}

def get_info(user_input):
    try:
        year, category = user_input.split()
        category = CATEGORIES[category]
        current_search = {"nobelPrizeYear": int(year), "nobelPrizeCategory": category}
    except ValueError:
        year = user_input
        current_search = {"nobelPrizeYear": int(year)}

    res = requests.get("http://api.nobelprize.org/2.1/nobelPrizes", params=current_search).json()
    return res

