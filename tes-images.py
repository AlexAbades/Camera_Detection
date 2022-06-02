# auxiliar code 

import numpy as np 
import pytesseract
from PIL import Image
import cv2 as cv 
import matplotlib.pyplot as plt 

def tesseract(impath):
    tespath =  r"C:\Program Files\Tesseract-OCR\tesseract"
    path_to_tesseract = tespath
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(Image.open(impath))
    print(text)
    return text 


path = '.\data\spa\spa1_06N.png'
I1 = Image.open(path) 
plt.imshow(I1)

# t = tesseract()