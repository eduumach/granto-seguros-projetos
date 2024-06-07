import re


def extract_data(text):
    patterns = {
    'processo': r'PROCESSO ELETRONICO SEI N\. (\d+\.\d+/\d+-\d+)',
    'contratante': r'CONTRATANTE: (.+?)(?:CNPJ)',
    'contratada': r'CONTRATADA: (.+?)(?:CNPJ)',
    'objeto': r'OBJETO: (.+?)(?:VALOR:)',
    'valor': r'VALOR: RS ([A-Z0-9]+)',
    'cnpj_contratante': r'CNPJ n\. (\d+\.\d+\.\d+/\d+-\d+)',
    'cnpj_contratada': r'CNPJ/MF sob n\. ([A-Z0-9]+)',
    'representante_contratante': r'(?<=representada pelo Sr\.) ([A-Za-z\s]+),',
    'representante_contratada': r'(?<=representada pelo Sr\.) ([A-Za-z\s]+),'
    }

    extracted_data = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.DOTALL)
        if match:
            extracted_data[key] = match.group(1).strip()

    return extracted_data