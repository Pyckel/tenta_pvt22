import requests
# Simon Söder

# Tips: använd sidan nedan för att se vilken data vi får tillbaks och hur apiet fungerar
# vi använder oss enbart av /nobelPrizes
# Dokumentation, hjälp samt verktyg för att testa apiet fins här: https://app.swaggerhub.com/apis/NobelMedia/NobelMasterData/2.1

HELP_STRING = """
Ange ett år och fält
Exempelvis 1965 fysik
"""

CATEGORIES = {"fysik": "phy",
       "kemi": "che",
       "litteratur": "lit",
       "ekonomi": "eco",
       "fred": "pea",
       "medicin": "med"}




# TODO 10p programmet skall ge en hjälpsam utskrift istället för en krasch om användaren skriver in fel input
# TODO 15p om användaren inte anger ett område som exempelvis fysik eller kemi så skall den parametern inte skickas med till apiet och vi får då alla priser det året


def main():
    help_text()
    while True:

        # TODO 5p Skriv bara ut hjälptexten en gång när programmet startar inte efter varje gång användaren matat in en fråga
        #      Förbättra hjälputskriften så att användaren vet vilka fält, exempelvis kemi som finns att välja på

        # TODO 5p Gör så att det finns ett sätt att avsluta programmet, om användaren skriver Q så skall programmet stängas av
        #      Beskriv i hjälptexten hur man avslutar programmet
        # TODO 5p Gör så att hjälptexten skrivs ut om användaren skriver h eller H
        user_input = input(">")
        year, category = user_input.split()
        category = CATEGORIES[category]

        category = {"nobelPrizeYear": int(year), "nobelPrizeCategory": category}

        res = requests.get("http://api.nobelprize.org/2.1/nobelPrizes", params=category).json()
        # TODO 5p  Lägg till någon typ av avskiljare mellan pristagare, exempelvis --------------------------

        # TODO 20p Skriv ut hur mycket pengar varje pristagare fick, tänk på att en del priser delas mellan flera mottagare, skriv ut både i dåtidens pengar och dagens värde
        #   Skriv ut med tre decimalers precision. exempel 534515.123
        #   Skapa en funktion som hanterar uträkningen av prispengar och skapa minst ett enhetestest för den funktionen
        #   Tips, titta på variabeln andel
        # Feynman fick exempelvis 1/3 av priset i fysik 1965, vilket borde gett ungefär 282000/3 kronor i dåtidens penningvärde

        for prize in res["nobelPrizes"]:
            prize_amount = prize["prizeAmount"]
            prize_amount_today = prize["prizeAmountAdjusted"]
            print(f"{prize['categoryFullName']['se']} prissumma {prize_amount} SEK")

            for person in prize["laureates"]:
                print(person['knownName']['en'])
                print(person['motivation']['en'])
                andel = person['portion']
                print('-' * 25)


def help_text():
    print(HELP_STRING)
    print('Alla möjliga kategorier:')
    key_list = list(CATEGORIES.keys())
    for i in key_list:
        print(i)


if __name__ == '__main__':
    main()
