import cv2

# threshold_image = cv2.threshold(image, thresh_value(0-255), max_value(255), method(most commonly.. THRESH_BINARY))

image = cv2.imread('CHAPTER 6\\sample.jpg', cv2.IMREAD_GRAYSCALE)

ret, thresh_img = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY)

cv2.imshow("Threshold Image", thresh_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# save
cv2.imwrite('thresh_img.jpg', thresh_img)

"""
90 - 0 Black
130 - 255 white
180 - 255 white
50 - 0 black
"""