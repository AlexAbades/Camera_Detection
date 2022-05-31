# Text detection using Teseract 

import cv2 as cv
from PIL import Image
from pytesseract import  pytesseract 



# Set to 0 to get default camera 
cap = cv.VideoCapture(0)

# Check if it's opening 
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    # Transform the image to black and white
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame', gray)
    
    # Create a exit key 
    if cv.waitKey(1) == ord('q'):
        # We should capture an image to detect the tesseract
        I1 = cv.imwrite('Image1.jpg', gray)
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()


def tesseract():
    print('hello i am being called')
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract"
    pathI1 = 'Image1.jpg'
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(Image.open(pathI1))
    print(text)

tesseract()
