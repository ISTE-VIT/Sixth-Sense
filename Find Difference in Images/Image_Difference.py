from skimage.metrics import structural_similarity as ssim
import imutils
import cv2

image1 = cv2.imread("pig1.png")
image2 = cv2.imread("pig2.png")
gray1 = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)

#ssim has two parameter i.e score and diff
(score,diff) = ssim(gray1, gray2, full=True)
diff = (diff*255).astype("uint8")
print("SSIM: {}".format(score))
#The difference image is currently represented as a floating point data type in the range [0, 1] 
#so we first convert the array to 8-bit unsigned integers in the range [0, 255] 
#before we can further process it using OpenCV.

#In thresholding, each pixel value is compared with the threshold value. 
# If the pixel value is smaller than the threshold, it is set to 0, otherwise, 
# it is set to a maximum value (generally 255).
thresh = cv2.threshold(diff,0,255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1] #Thresholding
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #Finding contours
cnts = imutils.grab_contours(cnts) #Grabbing contours

#we threshold our diff  image using both cv2.THRESH_BINARY_INV  and cv2.THRESH_OTSU β 
#both of these settings are applied at the same time using the vertical bar βorβ symbol, "|"
#A good threshold would be in the middle of those two values. 
#Similarly, Otsu's method determines an optimal global threshold value from the image histogram.

#now creating boundaries across the contours 
for c in cnts:
    (x,y,w,h) =  cv2.boundingRect(c)
    cv2.rectangle(image1,(x,y),(x+w,y+h), (0,0,255),2) #Drawing rectangle BGR thickness
    cv2.rectangle(image2,(x,y),(x+w,y+h), (0,0,255),2)  #Drawing rectangle BGR  thickness
    
cv2.imshow("Image-1", image1)
cv2.imshow("Image-2", image2)
cv2.imshow("Difference Between Images", diff)
cv2.imshow("Threshold", thresh)
cv2.waitKey(0)








