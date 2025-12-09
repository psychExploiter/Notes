import cv2

image = cv2.imread('CHAPTER 5\\before_median.jpg')

if image is None:
    print('Error could not find image.')
    
else:
    # cv2.medianBlur(image, kernal_size)
    after_median = cv2.medianBlur(image, 5)  # should be odd
    # replacing each pixel with the middle value 
  
    cv2.imshow('Blurred Image', after_median)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # save
    cv2.imwrite('after_median.jpg',after_median)