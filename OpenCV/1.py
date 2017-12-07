import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('watch2.jpg',cv2.COLOR_BGR2GRAY)
#IMREAD_COLOR  = -1
#IMREAD_UNCHANGED = -1
cv2.imshow('fv',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
plt.imshow(img ,cmap='gray',interpolation='none')
plt.plot([50,100],[80,100],'c',linewidth=5)
plt.show()
cv2.imwrite('sxd.png',img)

