import cv2

image = cv2.imread('CHAPTER 5\\sample.jpg')

if image is None:
    print('Error could not find image.')
    
else:
    blurred_image = cv2.GaussianBlur(image, (21,21), 3) # should always be odd
    # (3,3) light blur
    # (9,9) strong blur
    # (21,21) super strong blur
    # blurred_image = cv2.GaussianBlur(image, (kernel_size_x, kernel_size_y), sigma)
    
    cv2.imshow('Blurred Image', blurred_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # save
    cv2.imwrite('blurred_image.jpg',blurred_image)