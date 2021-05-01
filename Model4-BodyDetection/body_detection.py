import cv2

cap=cv2.VideoCapture(0)
while True:
    _,frame=cap.read()
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    lap=cv2.Laplacian(grayFrame,cv2.CV_64F)
    x_sobel=cv2.Sobel(grayFrame,cv2.CV_64F,1,0,ksize=5)
    y_sobel=cv2.Sobel(grayFrame,cv2.CV_64F,0,1,ksize=5)
    edges=cv2.Canny(grayFrame,200,200)

    cv2.imshow('Original',frame)
    cv2.imshow('Laplacian',lap)
    cv2.imshow('horizontal gradient',x_sobel)
    cv2.imshow('vertical gradient',y_sobel)
    cv2.imshow('Edge',edges)

   
    k=cv2.waitKey(5)

    if k==27:
        break;

cv2.destroyAllWindows()
cap.release()
