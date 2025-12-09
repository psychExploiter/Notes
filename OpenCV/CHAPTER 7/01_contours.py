# edges ko dhundne ki process ko contour kehte hai
# contours(list of all points detected in a shape),hierarchy(cotnour level's info parent to child) = cv2.findContours(image(binary), mode(retrieval mode ex. RETR_TREE, RETR_ExTERNAL), method(chain approx simple))
# binary image = black and white image
# mode: how many counters and what kind of
# RETR_EXTERNAL : returns only outermost shape (suppose you have two squares one inside other, it will only give the outside one)
# RETR_TREE : every shape (outer square and innner square and who is inside who)
# RETR_LIST : all contours but without hierarchy
# method : how much detail for each contour (chain approx simple [only stores corner points to save memory], (chain approx null) [it stores every pixel of contour])

import cv2

img = cv2.imread('CHAPTER 7\\Rectangle.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

# _ is a placeholder

# Find contours
contours, heirarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # now it knows where is the borders of shape
# to output the contours

# cv2.drawContours(image, contours, contour_index, color, thickness)
# contour_index = -1 (draw everything), 0(first), 1(second)

cv2.drawContours(img, contours, -1, (0,255,0), 3)

cv2.imshow("Contours", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# save

cv2.imwrite("contours.jpg", img)