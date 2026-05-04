print("Hallo,World")
def berechne_netto_preis(brutto, steuersatz=19):
    netto = brutto / (1 + steuersatz / 100)
    netto = round(netto, 2)
    return netto
print("cisco")