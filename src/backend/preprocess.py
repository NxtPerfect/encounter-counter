import re
import cv2
import numpy as np
import pytesseract as pytes
from pytesseract import Output
from src.constants import SRC_ROOT_DIR
from PIL import Image
from pathlib import Path

"""
Frist i should upscale the image, with 1080p monitor height, the font
is about 14pixels high, while it should be no less than 20
"""
def preprocessImage(imagesPath:str = SRC_ROOT_DIR + "/../assets/"):
    imagePaths = ["testSingle.png", "testSingle2.jpg", "testSingle3.jpg", "testMultipleShiny.png", "testMultipleShinyMobile.jpg", "testMultipleShinyMobile2.png"]
    for imagePath in imagePaths:
        preresizedImagePath = Path(SRC_ROOT_DIR + f"/../assets/{imagePath}")
        resizedImagePath = Path(SRC_ROOT_DIR + f"/../assets/resized{imagePath}")
        if (not resizedImagePath.is_file()):
            image = Image.open(preresizedImagePath)
            im = upscale(image)
        image = cv2.imread(resizedImagePath)
        im = canny(erode(thresholding(grayscale(image))))

        pokemonNameAndLevelPattern = r'^(\w+)\sLv\.\s\d{1,3}'

        h, *args = im.shape
        boxes = pytes.image_to_boxes(im)
        for b in boxes.splitlines():
            b = b.split(' ')
            img = cv2.rectangle(im, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (255, 0, 0), 2)
        cv2.imshow('img', img)
        cv2.waitKey(0)

        # custom_config = r'-l eng --oem 3 --psm 6'
        # print(pytes.image_to_string(img, config=custom_config))

        d = pytes.image_to_data(im, output_type=Output.DICT)
        n_boxes = len(d['text'])

        for i in range(n_boxes):
            if int(d['conf'][i]) > 60:
                if re.match(pokemonNameAndLevelPattern, d['text'][i]):
                    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                    img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    print(d['text'][i])
        cv2.imshow('img', img)
        cv2.waitKey(0)

        custom_config = r'-l eng --oem 3 --psm 6'
        print(pytes.image_to_string(img, config=custom_config))

def upscale(image):
    pass
    base_width = 4096
    wpercent = (base_width / float(image.size[0]))
    hsize = int((float(image.size[1]) * float(wpercent)))
    img = image.resize((base_width, hsize), Image.Resampling.LANCZOS)
    if image.format in ["JPEG", "JPG"]:
        img.save(f"assets/resized{image.filename.split('/')[-1]}", "JPEG")
        return img
    img.save(f"assets/resized{image.filename.split('/')[-1]}")
    return img

def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def removeNoise(image):
    return cv2.medianBlur(image, 5)

def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

def dilation(image):
    kernel = np.ones((5,5), np.uint8)
    return cv2.dilate(image, kernel, iterations=1)

def erode(image):
    kernel = np.ones((5,5), np.uint8)
    return cv2.erode(image, kernel, iterations=1)

def opening(image):
    kernel = np.ones((5,5), np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

def canny(image):
    return cv2.Canny(image, 100, 200) # 50, 200, default 100, 200

def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w//2, h//2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated

if __name__ == "__main__":
    preprocessImage()
