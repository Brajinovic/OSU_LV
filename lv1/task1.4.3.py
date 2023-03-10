print("################### Početak programa ############################")
print("################## By Ivan Brajinović ###########################")
print("####################### FERIT 2023 ##############################")

brojevi = []

while True:
	try:
		print("Unesi broj: ", end=" ")
		broj = input()
		if(broj == "Done"):
			break
		broj = int(broj)

	except ValueError:
		print("Unos nije broj!")

	else:
		brojevi.append(broj)

print(f"Korisnik je unio {len(brojevi)} brojeva")
print(f"Srednja vrijednost: {sum(brojevi) / len(brojevi)}")
print(f"Minimalna vrijednost: {min(brojevi)}")
print(f"Maksimalna vrijednsot: {max(brojevi)}")
brojevi.sort()
[print(x, end=" ") for x in brojevi]