import numpy as np
import cv2

img = cv2.imread('img2.jpg')
median = cv2.medianBlur(img, 5)
compare = np.concatenate((img, median), axis=1)

cv2.imshow('image',compare)
cv2.waitKey(0)
cv2.destroyAllWindows()