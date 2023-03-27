import time
import cv2
from PIL import Image
import pytesseract
import numpy as np
from PIL import ImageGrab


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

while True:
    img = ImageGrab.grab()
    top = (img.height - 500) // 2
    img = img.crop((650, top, 1900, 870))

    lower_red = np.array([230, 0, 0]) # lower red
    upper_red = np.array([255, 150, 50]) # upper red
    lower_yellow = np.array([240, 180, 35]) # lower yellow
    upper_yellow = np.array([255, 220, 120]) # upper yellow

    red_mask = cv2.inRange(np.array(img), lower_red, upper_red)

    yellow_mask = cv2.inRange(np.array(img), lower_yellow, upper_yellow)

    a = pytesseract.image_to_string(yellow_mask, lang='pol')
    b = pytesseract.image_to_string(red_mask, lang='pol')
    a = a[:-1]
    b = b[:-1]
    #print(a[0:2])

    def save(event):
        f = open(r"output.txt", "r+")
        lines = f.readlines()
        f.seek(0) # move to the beginning of the file
        f.truncate()
        for line in lines:
            elements = line.strip().split('/')
        if event == 'win':
            elements[0] = str(int(elements[0]) + 1)  # increase first element by 1
            f.write('/'.join(elements) + '\n')  # save to file
        elif event == 'lose':
            elements[1] = str(int(elements[1]) + 1)  # increase second element by 1
            f.write('/'.join(elements) + '\n')  # save to file
    

    if a[0:2] == "ZW":
        print("asdasdas")
        save('win')
        time.sleep(10)
    elif b[0:2] == "PO":
        print("asdasdasyyyyy")
        save('lose')
        time.sleep(10)
    time.sleep(0.25)
