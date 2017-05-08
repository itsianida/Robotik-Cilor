import cv2
import numpy as np

#inisialisasi camera
cap= cv2.VideoCapture(0)
#produksi output
fourcc = cv2.VideoWriter_fourcc(* 'XVID')
out = cv2.VideoWriter("hasil.avi", fourcc, 20.0, (640, 480))

#kondisi kamera menyala
while True:
    ret, frame = cap.read()
    #menunjukkan frame di layar pc
    out.write(frame)
    cv2.imshow('frame', frame)

#kondisi berhenti
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows
