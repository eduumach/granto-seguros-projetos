import pytesseract
from PIL import Image

def read_text_from_image(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text


if __name__ == "__main__":
    image_path = '../files/exp_page_01.jpg'
    document_text = read_text_from_image(image_path)
    print(document_text)
