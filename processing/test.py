from read import read_scanned_pdf_op2, read_file_pdf, read_file_word, read_image
from text_processing import regex


if __name__ == "__main__":
    file_path = 'files/exp_word.docx'

    document_text = read_file_word.read_word_file(file_path)
    extracted_data = regex.extract_data(document_text)
    # print("Document text:", document_text)
    # print("Extracted data:", extracted_data)
    for key, value in extracted_data.items():
            print(f"{key}: {value}")