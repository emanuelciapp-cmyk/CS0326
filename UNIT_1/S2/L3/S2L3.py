
print("Scegli la figura di cui vuoi calcolare il perimetro: ")
figura = input("-QUADRATO- -CERCHIO- -RETTANGOLO-")
figura = figura.upper()
if(figura=="QUADRATO"):
    lato = float(input("Lato: "))
    print(f"Il perimetro del quadrato è {lato*4}")

elif(figura=="CERCHIO"):
    raggio = float(input("Raggio: "))
    print(f"La circonferenza del cerchio è {2*3.14*raggio}")

elif(figura=="RETTANGOLO"):
    altezza = float(input("Altezza: "))
    base = float(input("Base: "))
    print(f"Il perimetro del rettangolo è {(base*2)+(altezza*2)}")


