import numpy as np
import matplotlib.pyplot as plot


data = np.loadtxt("data.csv", delimiter=",", skiprows=1)

#na koliko osoba su izvršena mjerenja
print(f"Mjerenja su izvršena na {data.shape[0]} osoba")

#prikazite odnos visine i mase osobe
visina = data[:,1]
print(visina)
masa =  data[:,2]

plot.scatter(visina, masa, s=1)
plot.xlabel("Visina osobe")
plot.ylabel("Masa osobe")
plot.title("Odnos visine i mase osobe")
plot.show()

visinaa = visina[::50]
print(visina)
masaa =  masa[::50]

plot.scatter(visinaa, masaa, s=1)
plot.xlabel("Visina osobe")
plot.ylabel("Masa osobe")
plot.title("Odnos visine i mase osobe")
plot.show()

#minimalna, maksimalna, srednja vrijednost
print(f"Minimalna vrijednost visine: {min(visina)}\n Maksimalna vrijednost visine: {max(visina)}\n Srednja vrijednost visine: {np.mean(visina)}")

#mudonje
visina = [x for x in visina if data[:,0][visina.index(x)] == 1.0]

print(f"Minimalna vrijednost visine: {min(visina)}\n Maksimalna vrijednost visine: {max(visina)}\n Srednja vrijednost visine: {np.mean(visina)}")
