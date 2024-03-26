from PIL import Image
import pytesseract
import numpy as np
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

for img in os.listdir('photos'):
    image = Image.open(f'photos/{img}')
    text = pytesseract.image_to_string(image)
    with open(f'results/{img}.txt', 'w', encoding='utf-8') as result:
        result.write(text)