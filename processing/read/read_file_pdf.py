import fitz

def read_pdf_file(file_path):
    doc = fitz.open(file_path)
    
    full_text = []
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        full_text.append(page.get_text())
    
    return '\n'.join(full_text)

if __name__ == "__main__":
    file_path = '../files/exp-not-image.pdf'

    document_text = read_pdf_file(file_path)
    print(document_text)