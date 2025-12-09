# canny edge detection : is used for detecting edges or outlines from an image (such as a circle)
# image thresholding : it converts complex images to clean B&W images (used in object detection, masking)
# Bitwise Operations : Combining images, cutting shapes logically

#############################################################################################################

# canny edge detection:
# edges = cv2.Canny(image, threshold1, threshold2) 
# threshold1 is lower boundary (to detect weak edges)
# threshold 2 is upper boundary (for strong edges)
# like if pixel is higher than the threshold value white it fully if it is below it then black it

# Used for:
# detect borders
# Seperate objects
# feature extraction
# face recognition and lane tracking
# sketch effect on an image

import cv2

image = cv2.imread('CHAPTER 6\\sample.jpg', cv2.IMREAD_GRAYSCALE)

edges = cv2.Canny(image, 50, 150)

cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

# save

cv2.imwrite('edges.jpg', edges)