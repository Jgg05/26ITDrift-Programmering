navn = input("Hva heter du? ")
belop = int(input("Hvor mye vil du sette inn? (hele kroner) "))
rente = float(input("Hva er renten i prosent? "))

print("Hei, " + navn + "!")
print("Du har satt inn " + str(belop) + " kroner.")
print("Renter: " + str(rente) + "%")
print("Etter ett år vil du ha " + str(belop * (1 + rente / 100)) + " kroner.")
