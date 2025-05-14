from bs4 import BeautifulSoup
import traceback
import os
from escrever_excel import main as excel
class main(excel):
    def __init__(self):
        pass

    def lerHtml(self):
        try:
            nomearquivo = "C:\\Users\\rodri\\Assistente\\html"
            folder = os.listdir(nomearquivo)
            for arquivo in folder:
                caminho = os.path.join(nomearquivo, arquivo)

                with open(caminho, "r", encoding="utf-8") as file:
                    arq = file.read()
                    
                    soup = BeautifulSoup(arq, "html.parser")
                    data: str = self.data(soup)
                    origem: str = self.origem(soup)  
                    destino: str = self.destino(soup)
                    pagamento: str = self.método(soup)   
                    categoria: str = self.categoria(soup)
                    valor_da_corrida: float = self.valor(soup)
                    self.programa(data, origem, destino, pagamento, categoria, valor_da_corrida)
                    
                               
        except:
            print(f"Erro na execução do programa {traceback.format_exc()}")

    def data(self, soup):
        data_td = soup.find("td", style="padding:40px 0 16px 0;")
        if data_td:
            span_data = data_td.find("span", style="font-size: 14px;line-height:17px;color:#000000;")
            if span_data:
                data = span_data.text.strip()
                return data
    
    def valor(self, soup):
        detalhes = soup.find("td", string="Detalhes da tarifa").find_parent("tr").find_parent("tbody").find_parent("table")
        if detalhes:
            linha_valor = detalhes.find("td", string="Valor da corrida").find_parent("tr")

            if linha_valor:
                celulas = linha_valor.find_all("td")
                if len(celulas) == 2:
                    valor = celulas[1].text.strip()
                    valor = str(valor[2:]).replace(",", ".")
                    return valor
                
    def origem(self, soup):
        hora_origem = soup.find("div", style=lambda value: value and "color: #000000;" in value)
        origem = soup.find("div", style= lambda value: value and "color: #5C6166;" in value)
        if origem:
            return f"{origem.text}, {hora_origem.text}"

    def destino(self,soup):
        hora_destino = soup.find("td", valign="top", style="")
        if hora_destino:
            hora = hora_destino.find("div", style=lambda value: value and "color: #000000;" in value)
            destino = hora_destino.find("div", style=lambda value: value and "color: #5C6166;" in value)
            if hora and destino:
                return f"{destino.text}, {hora.text}"
    def método(self, soup):
        metodo = soup.find("td", style="padding-bottom:25px; color: #5C6166;font-size: 14px; margin-top: 10px;word-break: break-word;line-height:14px;")
        if metodo:
            span = metodo.find("span")
            if span:
                metodo_pag = span.text
                return metodo_pag
    
    def categoria(self, soup):
        categoria = soup.find("td", style="padding:0;width:34px")
        if categoria:
            irmão = categoria.find_next_sibling("td", style="padding:0;padding:0;")
            if irmão:
                strong = irmão.find("strong")
                if strong:
                    span = strong.find("span")
                    if span:
                        return span.text
if __name__ == "__main__":
    program = main()
    program.lerHtml()