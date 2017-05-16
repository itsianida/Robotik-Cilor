import cv2
import numpy as np

gambar = cv2.imread("asli3.jpg",0)
#cv2.imshow("gambar",gambar)
gambar2 = cv2.imread("coba3.2.jpg",0)
#print(gambar[1,1])
c = gambar.shape
kecurigaan = 0
for i in range(0,c[0]):
	for j in range(0,c[1]):
		if (gambar2[i,j]<=gambar[i,j]-50 or gambar2[i,j]>=gambar[i,j]+50):
			kecurigaan=kecurigaan+1
			gambar2[i,j]=255
#cv2.imshow("gambar1",gambar)
cv2.imshow("ada nadia",gambar2)
print(kecurigaan)
print(gambar.shape)
print(720*1280)
cv2.waitKey(0)
cv2.destroyAllWindows 