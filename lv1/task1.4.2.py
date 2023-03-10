print("################### Početak programa ############################")
print("################## By Ivan Brajinović ###########################")
print("####################### FERIT 2023 ##############################")

print("Unesite ocjenu između 0.0 i 1.0: ", end="")

try:
	ocjena = float(input())

except ValueError:
	print("Unos nije broj!")

else:
	if ocjena > 1.0 or ocjena < 0.0:
		print("Unešena ocjena se nalazi izvan dopuštenog intervala [0.0, 1.0]!")
		
	else:
		print("Kategorija ocjene: ", end="")
		if ocjena >= 0.9:
			print("A")

		elif ocjena >= 0.8:
			print("B")

		elif ocjena >= 0.7:
			print("C")

		elif ocjena >= 0.6:
			print("D")

		else:
			print("F")
