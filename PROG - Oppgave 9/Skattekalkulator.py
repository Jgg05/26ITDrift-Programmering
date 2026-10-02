# Programmet beregner skatt og nettolønn ut fra brutto årslønn.
# Brukeren avslutter ved å skrive inn en negativ årslønn.
from Grenser_for_Skatteprosenter import Grenser_for_Skatteprosenter

# Les inn den første brutto årslønnen.
bruttolønn = float(input("Skriv inn brutto årslønn (eller et negativt tall for å avslutte): "))

while bruttolønn >= 0:
    # Finn riktig skatteprosent ut fra grensene.
    skatteprosent = Grenser_for_Skatteprosenter(bruttolønn)

    # Beregn skatt og lønn etter skatt.
    skatt = bruttolønn * skatteprosent / 100
    nettolønn = bruttolønn - skatt

    # Skriv ut resultatene.
    print(f"Brutto årslønn: {bruttolønn:.2f} kr")
    print(f"Skatteprosent: {skatteprosent} %")
    print(f"Skatt: {skatt:.2f} kr")
    print(f"Netto årslønn: {nettolønn:.2f} kr")
    print(f"Omtrentlig månedslønn etter skatt: {nettolønn / 12:.2f} kr")
    print("-----------------------------")

    # Les inn neste årslønn, eller et negativt tall for å avslutte.
    bruttolønn = float(input("Skriv inn brutto årslønn (eller et negativt tall for å avslutte): "))


print("Skattekalkulatoren er avsluttet.")