import cv2

load = cv2.imread('upin.jpeg', 1)
flip = cv2.flip(load, 0)

cv2.imshow('Gambar', flip)

cv2.waitKey(0)
cv2.destroyAllWindows()