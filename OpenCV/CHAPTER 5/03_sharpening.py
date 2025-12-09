import cv2
import numpy as np

image = cv2.imread('CHAPTER 5\\after_median.jpg')

sharpen_kernel = np.array(
    [[0,-1, 0],
     [-1, 5,-1],
     [0,-1,0]
     ])

if image is None:
    print('Error could not find image.')
    
else:
    # sharpening feature
    # sharpen_image = cv2.filter2D(src, ddepth, kernel) 
    sharpen_image = cv2.filter2D(image, -1, sharpen_kernel) 
    
    cv2.imshow('sharpen Image', sharpen_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # save
    cv2.imwrite('sharpen_image.jpg',sharpen_image)