
img= cv2.GaussianBlur(img, (5,5) , 0 )
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1)

laplacian = cv2.Laplacian(img, cv2.CV_64F, Ksize=5)

canny = cv2.Canny(img, 100 ,  150) 
