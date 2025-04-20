"""Objetivo do programa é criar um programa que leia uma nota fiscal comum primeiramente e depois
vai avançando para modelos mais avançados"""



"""Na nota fiscal de cnpj não há a chave nfeProc"""


"""Testar vários tipos de notas fiscais pois algumas não tem algumas informações do emissor"""

import xmltodict
import json

arquivo = "Nota/xml/country_data.xml"

with open(arquivo, "rb") as file:
    dic_arquivo = xmltodict.parse(file)
    print(json.dumps(dic_arquivo, indent=4))
    info = dic_arquivo["nfeProc"]["NFe"]["infNFe"]
    numero_nota = info["@Id"]
    emissor_nota = info["emit"]['xNome']
    dest = info['dest']["xNome"]
    endereço = info["dest"]["enderDest"]
    peso = info["transp"]["vol"]["pesoB"]


    print("Número da nota: ",numero_nota, "\nEmissor nota: ", emissor_nota, "\nCliente: ", dest,"\nEndereço: ", endereço,"\nPeso Bruto: " ,peso)