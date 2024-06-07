import re
import json


def extract_contract_info(text):
    pattern = re.compile(r'(?P<before>.*?)«(?P<inside>.*?)»(?P<after>.*)')
    matches = pattern.findall(text)
    
    result = {}
    
    for i, match in enumerate(matches, start=1):
        before, inside, after = match
        result[inside] = {1: after.strip(), 2: before.strip()}
    
    return result

if __name__ == "__main__":
    text = """
    CONTRATO N. «Numero_Contrato»
    PROCESSO ELETRÔNICO SEI N. 6014.2022/0003235-8 CONTRATANTE: SECRETARIA MUNICIPAL DE HABITAÇÃO - SEHAB
    CONTRATADA: «Nome_Contratada»
    OBJETO: CONTRATAÇÃO DE EMPRESA ESPECIALIZADA PARA A REFORMA E MELHORIA DO SISTEMA DE GÁS, DO SISTEMA DE PROTEÇÃO CONTRA DESCARGAS ATMOSFÉRICAS (SPDA) E DE COMBATE AO INCÊNDIO, PARA OBTENÇÃO DO AUTO DE VISTORIA DO CORPO DE BOMBEIROS (AVCB) DO CONJUNTO HABITACIONA CHÁCARA BELA VISTA.
    VALOR: R$ «Valor_Contrato» (sem desoneração).
    """

    result = extract_contract_info(text)
    print(json.dumps(result))