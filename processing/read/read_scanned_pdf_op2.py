import fitz
import pytesseract
from PIL import Image
import io

def read_scanned_pdf(file_path):
    doc = fitz.open(file_path)
    
    full_text = []
    
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        
        pix = page.get_pixmap()
        img = Image.open(io.BytesIO(pix.tobytes()))
        
        text = pytesseract.image_to_string(img)
        full_text.append(text)
    
    return '\n'.join(full_text)

if __name__ == "__main__":
    file_path = '../files/exp.pdf'

    document_text = read_scanned_pdf(file_path)
    print(document_text)