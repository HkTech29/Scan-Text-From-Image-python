from PIL import Image

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

test = pytesseract.image_to_string(Image.open('images/img1.jpg'))
print(test)