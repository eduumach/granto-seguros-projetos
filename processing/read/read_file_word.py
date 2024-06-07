from docx import Document

def read_word_file(file_path):
    doc = Document(file_path)
    
    full_text = []
    for paragraph in doc.paragraphs:
        full_text.append(paragraph.text)
    return '\n'.join(full_text)


if __name__ == "__main__":
    file_path = '../files/exp_word.docx'

    document_text = read_word_file(file_path)
    print(document_text)