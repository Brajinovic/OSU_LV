import numpy as np
import matplotlib.pyplot as plot


data = np.loadtxt("data.csv", delimiter=",", dtype=str)
data = data[1:]
data.sort()

#na koliko osoba su izvršena mjerenja
print(f"Mjerenja su izvršena na {data.shape[0]} osoba")

#prikazite odnos visine i mase osobe
visina = np.array([float(x[1]) for x in data])
masa = np.array([float(x[2]) for x in data])
plot.scatter(visina, masa)
plot.xlabel("Visina osobe")
plot.ylabel("Masa osobe")
plot.title("Odnos visine i mase osobe")
plot.show()
