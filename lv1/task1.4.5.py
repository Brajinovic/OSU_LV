print("################### Početak programa ############################")
print("################## By Ivan Brajinović ###########################")
print("####################### FERIT 2023 ##############################")

file = open("SMSSpamCollection.txt")
ham = []
spam = []
counter = 0
for x in file:
	x = x.strip()
	if(x.startswith("ham")):
		ham.append(len(x.split(" ")) - 1)
	else:
		spam.append(len(x.split(" ")) - 1)
		counter = counter + 1 if x[-1] == "!" else counter

print(f"\nProsječan broj riječi u 'ham' porukama je: {sum(ham) / len(ham)}")
print(f"Prosječan broj riječi u 'spam' porukama je: {sum(spam) / len(spam)}")
print(f"\nBroj SMS poruka tipa 'spam' koje završavaju sa uskličnikom(!) je: {counter}")