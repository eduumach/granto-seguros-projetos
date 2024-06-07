import fitz 
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import cv2
import numpy as np
import io

def enhance_image(image):
    image = image.convert('L')
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)
    image = image.filter(ImageFilter.SHARPEN)
    return image

def read_scanned_pdf(file_path):
    doc = fitz.open(file_path)
    
    full_text = []
    
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        
        pix = page.get_pixmap()
        img = Image.open(io.BytesIO(pix.tobytes()))
        
        img = enhance_image(img)
        
        img_cv = np.array(img)
        img_cv = cv2.cvtColor(img_cv, cv2.COLOR_GRAY2BGR)
        
        text = pytesseract.image_to_string(img_cv)
        full_text.append(text)
    
    return '\n'.join(full_text)

if __name__ == "__main__":
    file_path = '../files/exp-image.pdf'

    document_text = read_scanned_pdf(file_path)
    print(document_text)
