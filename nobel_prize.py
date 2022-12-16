from api import get_info, CATEGORIES

# Simon Söder


HELP_STRING = """
Ange ett år och fält
Exempelvis 1965 fysik
Skriv in Q för att avsluta
Skriv in H för att få fram hjälp texten och alla kategorier
"""


def main():
    # Frågar användaren efter en str och anropar funktionen som gör det användaren vill
    print_help_text()
    while True:
        user_input = input(">").lower()
        if user_input == 'q':
            print('Stänger ner programmet')
            break
        elif user_input == 'h':
            print_help_text()
        else:
            res = check_user_input(user_input)
            if res:
                print_selected_nobel_prizes(res)


def print_selected_nobel_prizes(res: dict):
    # skriver ut all information som användaren har begärt och skickar 2 str till calculate_prize_share för att få
    # tillbaka en float
    for prize in res["nobelPrizes"]:
        prize_amount = prize["prizeAmount"]
        prize_amount_today = prize["prizeAmountAdjusted"]
        print(f"{prize['categoryFullName']['se']} prissumma {prize_amount} SEK")
        print(f'Dagens värde på priset är {prize_amount_today}')
        for person in prize["laureates"]:
            if 'knownName' in person:
                print(person['knownName']['en'])
            else:
                print(person['orgName']['en'])
            print(person['motivation']['en'])
            andel = person['portion']
            print(f'Fick {calculate_prize_share(prize_amount, andel)} utav {prize_amount}')
            print('-' * 25)


def calculate_prize_share(prize_amount: str, andel: str) -> float:
    # Beräknar fram en float till 3 decimaler från två str som in data och klarar att andel är ett fraktal
    if '/' in andel:
        andel = andel.split('/')[-1]
    prize = int(prize_amount) / int(andel)
    prize = round(prize, 3)
    return prize


def check_user_input(user_input: str) -> dict:
    # Kontrollerar om användaren har skrivit in en giltigt str om str är giltigt så skickas informationen till get_info
    # annars så skrivs det ut ett felmeddelande till användaren och hur giltigt inmatning ser ut
    try:
        year, category = user_input.split()
        res = get_info(year, category)
    except ValueError:
        if user_input.isnumeric():
            year = user_input
            res = get_info(year)
        else:
            print('Skriv in bara ett årtal eller årtal mellanslag kategori')
            res = None
    return res


def print_help_text():
    # Skriver ut hjälp texten och alla kategorier i terminalen när programmet startar eller användaren skriv in h
    print(HELP_STRING)
    print('Alla möjliga kategorier:')
    key_list = list(CATEGORIES.keys())
    for i in key_list:
        print(i)


if __name__ == '__main__':
    main()
