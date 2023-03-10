import numpy as np
import matplotlib . pyplot as plt
img = plt . imread ( "road.jpg" )
img = img [ : ,: ,0 ] . copy ()
print( img . shape )
print( img . dtype )
plt.figure ()
plt.imshow ( img , cmap = "gray", alpha=0.4)
plt.show ()


img1 = img [ : ,int(img.shape[1]/4): int(img.shape[1]/2) ] . copy ()
print( img . shape )
print( img . dtype )
plt.figure ()
plt.imshow ( img1 , cmap = "gray", alpha=0.4)
plt.show ()

img2 = img.copy()
for i in range(0, 3):
    img2 = np.rot90(img2)

print( img . shape )
print( img . dtype )
plt.figure ()
plt.imshow ( img2 , cmap = "gray")
plt.show ()


print( img . shape )
print( img . dtype )
plt.figure ()
plt.imshow ( np.fliplr(img) , cmap = "gray")
plt.show ()