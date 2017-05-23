import cv2
import numpy as np
import sys


gambar = cv2.imread("asli.jpg",0)
gambar2 = cv2.imread("coba.jpg",0)
kecurigaan = 0
c  = gambar.shape
for i in range(0,c[0]):
	for j in range(0,c[1]):
		if (gambar2[i,j]<=gambar[i,j]-50 or gambar2[i,j]>=gambar[i,j]+50):
			kecurigaan=kecurigaan+1
			gambar2[i,j]=255

cv2.imshow("ada nadia",gambar2)
print(kecurigaan)
if kecurigaan>60000:
	sys.stdout.write('\a')
	sys.stdout.flush()
print (gambar.shape)
cv2.waitKey(0)
cv2.destroyAllWindows 