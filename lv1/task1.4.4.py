print("################### Početak programa ############################")
print("################## By Ivan Brajinović ###########################")
print("####################### FERIT 2023 ##############################")

file = open("song.txt")
wordOccurence = {}

for line in file:
	for x in line.split(" "):
		x = x.strip()
		if(x[-1] == ","):
			x = x[:-1]
		if x not in [i for i in wordOccurence]:
			wordOccurence[x] = 1
		else:
			wordOccurence.update({x: wordOccurence[x] + 1})

for i in wordOccurence:
	if wordOccurence[i] == 1:
		print(i)
