# Bitwise Operation
# 2 image combine
# cut out
# flip / remove

# cv2.bitwise_and(img1, img2) # cutout a shape from another (white areas)
# cv2.bitwise_or(img1, img2) # adding a new object
# cv2.bitwise_not(img) # white ko black, black ko white

# img1 img2 heigth width same
# use only black and white

import cv2
import numpy as np

img1 = np.zeros((300,300), dtype="uint8")
img2 = np.zeros((300,300), dtype="uint8")

cv2.circle(img1, (150,150), 100, 255, -1)

cv2.rectangle(img2, (100, 100), (250,250), 255, -1)

bitwise_and = cv2.bitwise_and(img1, img2)
bitwise_or = cv2.bitwise_or(img1, img2)
bitwise_not = cv2.bitwise_not(img1)

cv2.imshow("Circle", img1)
cv2.imshow("Rectangle", img2)
cv2.imshow("AND", bitwise_and)
cv2.imshow("OR", bitwise_or)
cv2.imshow("NOT", bitwise_not)
cv2.waitKey(0)
cv2.destroyAllWindows()

# # save
cv2.imwrite("Circle.jpg", img1)
cv2.imwrite("Rectangle.jpg", img2)
cv2.imwrite("AND.jpg", bitwise_and)
cv2.imwrite("OR.jpg", bitwise_or)
cv2.imwrite("NOT.jpg", bitwise_not)

