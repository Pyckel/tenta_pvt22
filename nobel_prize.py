from api import get_info, CATEGORIES

# Simon Söder

# Tips: använd sidan nedan för att se vilken data vi får tillbaks och hur apiet fungerar
# vi använder oss enbart av /nobelPrizes
# Dokumentation, hjälp samt verktyg för att testa apiet fins här:
# https://app.swaggerhub.com/apis/NobelMedia/NobelMasterData/2.1

HELP_STRING = """
Ange ett år och fält
Exempelvis 1965 fysik
Skriv in Q för att avsluta
Skriv in H för att få fram hjälp texten och alla kategorier
"""


def main():
    help_text()
    while True:

        user_input = input(">").lower()
        if user_input == 'q':
            print('Stänger ner programmet')
            break
        elif user_input == 'h':
            help_text()
        else:
            res = interpret_user_input(user_input)

            # TODO 20p Skriv ut hur mycket pengar varje pristagare fick, tänk på att en del priser delas mellan flera mottagare, skriv ut både i dåtidens pengar och dagens värde
        #   Skriv ut med tre decimalers precision. exempel 534515.123
        #   Skapa en funktion som hanterar uträkningen av prispengar och skapa minst ett enhetestest för den funktionen
        #   Tips, titta på variabeln andel
        # Feynman fick exempelvis 1/3 av priset i fysik 1965, vilket borde gett ungefär 282000/3 kronor i dåtidens penningvärde
            print_selected_nobel_prize(res)


def print_selected_nobel_prize(res):
    if res:
        for prize in res["nobelPrizes"]:
            prize_amount = prize["prizeAmount"]
            prize_amount_today = prize["prizeAmountAdjusted"]
            print(f"{prize['categoryFullName']['se']} prissumma {prize_amount} SEK")
            print(f'Dagens värde på prise är {prize_amount_today}')

            for person in prize["laureates"]:
                if 'knownName' in person:
                    print(person['knownName']['en'])
                else:
                    print(person['orgName']['en'])
                print(person['motivation']['en'])
                andel = person['portion']
                print(f'Fick {calculate_prize_share(prize_amount, andel)} utav {prize_amount}')
                print('-' * 25)


def calculate_prize_share(prize_amount, andel):
    if '/' in andel:
        andel = andel.split('/')[-1]
    prize = int(prize_amount) / int(andel)
    prize = round(prize, 3)
    return prize


def interpret_user_input(user_input):
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


def help_text():
    print(HELP_STRING)
    print('Alla möjliga kategorier:')
    key_list = list(CATEGORIES.keys())
    for i in key_list:
        print(i)


if __name__ == '__main__':
    main()
