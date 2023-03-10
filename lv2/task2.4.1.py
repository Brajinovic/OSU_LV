import numpy
import matplotlib.pyplot as plot

x = numpy.array([1.0, 3.0, 3.0, 2.0, 1.0])
y = numpy.array([1.0, 1.0, 2.0, 2.0, 1.0])

plot.plot(x , y, 'r', linewidth=6, marker="x", markersize=30)
plot.axis([0.0, 4.0, 0.0, 4.0])
plot.xlabel("x os")
plot.ylabel("y os")
plot.title("Primjer")
plot.show()