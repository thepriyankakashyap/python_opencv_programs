
import cv2
image = cv2.imread('MyPic.png')
cv2.imwrite('MyPic.jpg', image)

grayImage = cv2.imread('MyPic.png', cv2.CV_LOAD_IMAGE_GRAYSCALE)
cv2.imwrite('MyPicGray.png', grayImage)
