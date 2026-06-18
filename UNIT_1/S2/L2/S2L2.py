

citta = input("Nome della tua città di origine: ")
animale = input("Nome del tuo animale domestico: ")

citta = citta.lower()
citta = citta.capitalize()
animale = animale.lower()
animale = animale.capitalize()

nomeBand = citta + " " + animale

print(f"Il nome per la tua band potrebbe essere {nomeBand}")