import cv2
import matplotlib.pyplot as plt 
import numpy as np 
import imutils
# import teseract as ts


print(f"File one __name__ is {__name__}")

if __name__ == '__main__':
    print("It's working")

    im1 = cv2.imread("data/spa/spa1_01MO.jpg")
    cv2.imshow('Frame', im1) 
    cv2.waitKey()
    cv2.destroyAllWindows()
    
else:
    print('Nothing')