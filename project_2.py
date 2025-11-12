#MAJOR PROJECT - 2
#Smile Detection


import cv2
smile_cascade=cv2.CascadeClassifier('C:/Users/Suman/Desktop/RINEX_PROJs/major_proj_2/haarcascade_smile.xml') #importing haarcascade file


img=cv2.imread('mk-4.png') #reading image 
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

smiles=smile_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=89)
#SaleFactor and minNeighbors are tuning parameters for better image
#ScaleFactor can be in range or 0 to 1.5 and minNeighbors are in the range of 2 to 20/25


for x,y,w,h in smiles:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),5) #w-width & h-height

cv2.imshow('smile detection',img)
cv2.waitKey(0) #to view the output image permanently
cv2.destroyAllWindows()