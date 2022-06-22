###---AlluKoodaa---###

from datetime import datetime

def onko_validi(hetu):
    tarkisteet = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    if len(hetu) != 11:
        return False
    if hetu[-5] not in "+-A":
        return False
    p = hetu[:2]
    k = hetu[2:4]
    v = ""
    if "-" in hetu:
        sep = "-"
        v += "19"
    elif "+" in hetu:
        sep = "+"
        v += "18"
    elif hetu[-5] == "A":
        sep = "A"
        v += "20"
    v += hetu[4:6]
    try:
        syn = datetime(int(v), int(k), int(p))
    except ValueError:
        return False
    merkki = hetu[-1]
    jono = "".join([x for x in hetu[:-1].split(sep, 1)])
    index = int(jono) % 31
    if merkki != tarkisteet[index]:
        return False
    return True

def main():
    hetu = input("Syötä henkilötunnus: ")
    print("Testataan...")
    tulos = onko_validi(hetu)
    if tulos:
        print("Henkilötunnus on validi!")
    else:
        print("Henkilötunnus ei ole validi!")
    laskuri = 0
    while True:
        syote = input("Kokeile uudestaan (Y/n)? ")
        if syote.casefold() == "y":
            print("Uusi yritys!")
            main()
        elif syote.casefold() == "n":
            print("Lopetetaan...")
            break
        else:
            laskuri += 1
            if laskuri == 0:
                print("Valitse \"Y\" tai \"n\"")
            elif laskuri == 10:
                print("eI väKiSIn!")
                raise RuntimeError("Käyttäjä on iha tyhäm")
            else:
                print(f"Olet syöttänyt {laskuri} kertaa väärän syötteen. Onnittelut.")
            continue
            
main()

###---eof---###
