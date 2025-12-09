# to detect shapes (by counting their corners)
# approx = cv2.approxPolyDP(contour, epsilon, True)
# (epsilon - 0.01)*cv2.arcLength(contour, True), (smaller = more precise, more points) (larger = rougher, fewer points)
# shape = small, arcLength = 200px, epsilon = 0.01 == 2.0px
# shape = large, arcLength = 800px, epsilon = 0.01 == 8.0px


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

# approxPolyDP

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    
    corners = len(approx)
    
    if corners == 3:
        shape_name = "Triangle"
    elif corners == 4:
        shape_name = "Rectangle"
    elif corners == 5:
        shape_name = "Pentagone"
    elif corners > 5:
        shape_name = "Circle"
        
    else: 
        shape_name = "unknown"
    
    cv2.drawContours(img, [approx], 0, (0,255,0), 2)
    x = approx.ravel()[0] # multidimensional array to 1D array
    y = approx.ravel()[1] - 10
    cv2.putText(img, shape_name, (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255,0,0), 2)
    
cv2.imshow("Contours", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# save

cv2.imwrite('detected_shape.jpg', img)

# 4:22:08