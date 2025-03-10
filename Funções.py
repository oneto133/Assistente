try:
  """
  Coloquei dentro de um tratamento de erros para não precisar instalar
  """
  from IPython.display import clear_output # type: ignore
  from pdf2docx import Converter as pdf # type: ignore
  from PIL import ImageTk, Image # type: ignore
  

except:
  from time import sleep
  from tkinter import filedialog, messagebox
  from string import ascii_uppercase, ascii_lowercase
  from datetime import datetime
  import pandas as pd
  from datetime import date
  import pytz, os, platform


class Tempo:
  def hora(self):
    '''
    Formatting the time because when using the datetime, it was getting a different time zone

    hora_atual: get the hour

    fuso_sao_paulo: get my timezone

    horameufuso: unites the fuso and the hour

    hora_formatada: formatting the hour

    apenashora: only get the hour to know what time is
    '''
    hora_atual = datetime.datetime.now(datetime.timezone.utc)
    fuso_sao_paulo = pytz.timezone('America/Sao_Paulo')
    horameufuso = hora_atual.astimezone(fuso_sao_paulo)
    hora_formatada = horameufuso.strftime("%H:%M:%S")
    apenashora = int(hora_formatada[:2])
    #Saudação
    if apenashora > 13 and apenashora < 18:
      #print("Boa tarde ", end=" ")
      return "Boa tarde " + hora_formatada

    elif apenashora >= 18 and apenashora <= 23:
      #print("Boa Noite! ", end="")
      return "Boa Noite! " + hora_formatada

    elif apenashora >= 00:
      #print("Bom dia ", end="")
      return "Bom dia " + hora_formatada


  def hora_atual(self):
    """
    Show de hour with minutes and seconds
    """
    agora = datetime.now()
    return agora.strftime("%H:%M:%S")

  def data_atual(self):
    agora = datetime.now()
    return agora.strftime("%d/%m/%Y")
  
  def Dias_da_semana(self, indice=bool):
    hoje = date.today()
    dia_da_semana = hoje.weekday()
    dias_da_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
    if indice:
      return dia_da_semana
    else:
      return dias_da_semana[dia_da_semana]


class Funcao():
  def __init__(self):
    pass

  def Tratar_Peso_Altura(self, valor, max, tam, nome):
    valor = str(valor)
    pos = valor.find(".")
    if int(valor[:pos]) > max:
      return f"505 {nome} maior que o permitido"

    else:
      if len(valor[pos:])> tam:
        valor = valor.replace(".", "")
        valor = valor[:6]
        valor = float(valor[:pos] + "." + valor[pos:pos+3])
        return valor

      else:
        peso = float(valor)
        return valor

  #Função de saida, acionada pra exibir dados indicando um termino do programa
  def sair(self):
    print("Saindo do programa, até mais...")
    sleep(1)
    print("Finalizado com êxito!")

  #Essa função serve para limpara a tela, não deixando o terminal cheio
  #permitindo uma melhor vizualização dos dados
  #Adaptada para diversos tipos de terminais e sistemas
  def Limpar_Tela(self):
    '''
    Limpar a tela do terminal para melhor vizualização
    de dados
    clear_output() -> Tenta limpar a tela caso
    o programa esteja sendo executado pelo google colab
    (onde esse código foi desenvolvido)

    os.system('cls') -> Tenta limpar a tela no windows
    caso a tentativa anterior precendida pela função Try não funcione

    caso a segunda tentativa precendida pela função Try não funcione
    os.system('clear') -> Tenta limpar a tela no linux

    No except temos a mensagem exibida indicado que não será possível limpar
    a tela, assim dando continuidade no programa
          '''
    try:
      os.system('cls')
    except:
      try:
        os.system('cls')
        clear_output()
      except:
        try:
          os.system('clear')
        except:
          print("Não foi possível limpar a tela")
    self.hora_calculo = Funcao().hora()
    self.hora_calculo = self.hora_calculo.replace(":", ".")



  def Alerta_Mensagem(self):
    mensagem1 = "Peso incorreto. "
    mensagem2 = "Altura incorreta. "
    mensagem3 = "Insira um peso apenas com números.\nExemplo:\n   127,65 ou 65.78\nSe precisar sair do programa, a qualquer momento digite SAIR."
    return mensagem1, mensagem2, mensagem3

  #Simples função de interrupção do programa quando precisarmos forçar
  #esse comando
  def Interromper(self):
      raise KeyboardInterrupt


  def Sair_Voltar(self, valor):
    '''
    Essa função é responsável por, de acordo com a preferencia do usuário,
    sair ou voltar para o topo do programa a hora que quiser
    '''
    valor = valor[:2]
    if valor == "SA":
      Funcao().sair()
      Funcao().Interromper()

    elif valor == "VO":
      Funcao().Limpar_Tela()
      return True

    else:
      pass


  def Tratar_Caracteres(self, valor):
    '''
    Aqui temos um tratamento de caracteres para que mais a frente
    no código seja possível converter os dados recebidos em string para float
    detalhe, os dados recebidos como string, só pode ser convertido para float
    se forem digitado com ponto ("."), pois esse é o padrão do python
    quando digitada uma vírgula (",") o python não reconhece
    assim fazemos esse trtamento para obter uma conversão correta
    '''
    valor = str(valor)
    valor = valor.replace(")", "").replace("(", "").replace("'", "")
    
    return valor


class Arquivo():

  def Verificar_se_existe_o_arquivo(self, arquivo):
      '''Vai na memóriado sistema operacional buscar o arquivo com o caminho fornecido, se o caminho existir, 
    retorna que sim, se não, retorna que não'''
      if os.path.exists(arquivo):
          return f"O Arquivo '{arquivo}' existe"
      else:
          print(f"O arquivo '{arquivo}'não existe...")
          
          return '1'
  def abrir_gerenciador_de_arquivos(self, caminho='diretorios.csv'):
    '''
    Criando um arquivo de cache
    '''
    with open(f'{caminho}', 'w') as dircsv:
        destino = filedialog.askopenfilenames(title = 'Salvar arquivo como',
        defaultextension='.pdf', filetypes=[("Arquivo PDF", "*.pdf"), ("All Files", "*")])
        dircsv.write(f'origem, destino\n{destino}')

  def ler_arquivo_em_cache(self, caminho='diretorios.csv'):
    '''
    Fonecer crie um arquivo em cache, se não criar, será usado um arquivo padrão
    ex, c:caminho.csv
    '''
    with open(f'{caminho}', 'r') as local:
      for c in local:
          if c[0] == '(':
              if c[2:-4] == "":
                return "vazio"
              else:
                return c[2:-3]
  def converter_arquivo(self, arquivo):
    cv = pdf(arquivo)
    cv.convert()

  def abrir_gerenciador_de_arquivos_para_destino(self):
    caminho = filedialog.askdirectory()
    return caminho
  
  def abrir_arquivo_gerado(self, caminho):
    sistema = platform.system()
    try:
      if sistema == "Windows":
        os.startfile(caminho)
      
      elif sistema == "Darwin":
        os.system(f"open '{caminho}'")
      
      else:
        os.system(f"xdg-open '{caminho}'")

    except Exception as e:
      return e

  def excluir(self, caminho):
    try:
      os.remove(caminho)
      return "Arquivo removido com sucesso!"
    except FileNotFoundError:
      return "Arquivo não encontrado"
    except PermissionError:
      return "Não permitido pelo sistema!"
    except OSError as e:
      return f"Erro: {e}"
class Graficos:
  def __init__(self):
    pass


  def Adicionar_imagens_nas_telas(self, imagem, altura=30, largura=30):
    """
    Adiciona imagens nas telas
    imagem: Fornceça o caminho da imagem
    altura: forneça a altura, padrão 30
    """
    self.imagem = Image.open(imagem)
    self.imagem = self.imagem.resize((altura, largura))
    self.foto= ImageTk.PhotoImage(self.imagem)
    return self.foto

class Tratamento_de_strings:
  def alfabeto_para_dicionarios(self, indice=0):
    alfabeto = ascii_uppercase
    return alfabeto[indice]
  
  def tratar_dados_de_url(self, texto_a_tratar):
    """
    Trata valores de para me retornar em formato de texto e apenas o que eu quero
    os valores qye vem pra cá são tirados de uma url usando a class div, então com o text
    eu obtenho só o resultado exibido na url
    """
    try:
      texto = str(texto_a_tratar.text.split())
    except:
      texto = str(texto_a_tratar)

    texto_sem_aspas = texto.replace("'", "").replace(",", "")
    texto_tratado = texto_sem_aspas[1:-1]
    return texto_tratado
  
  def tratar_valores_url(self, valor, porcentagem):
    """"
    essa função apenas faz um calculo de porcentagem para mim utilizando de outra função que tem nessa classe
    eu apenas to salvando essas funções aqui, para que eu possa organizar meu código principal e caso eu precise
    de apoio no futuro.
    """
    try:
      preço = float(self.tratar_dados_de_url(valor)[2:])
      divisor = float(self.tratar_dados_de_url(porcentagem)[:-1])
    except:
      return "Erro"
    resultado = preço * (divisor / 100)
    return resultado

class csv:
  def __init__(self):
    pass
  def escrever_csv(self, conteudo=str(), nome="arquivo.csv",
                   tipo="w", separador=";"):
    try:
      texto = str(conteudo)
      texto_tratado = texto.replace("(", "").replace(")","").replace("'","")
      with open(nome, tipo) as file:
        file.write(f"{texto_tratado}\n")
    except:
      print("erro")
  
  def ler_csv(self, nome, coluna, separador=","):
    self.df = pd.read_csv(nome, encoding="latin1", sep=separador)
    
    return self.df[coluna]
  
  def tipo(self, nome, coluna, igual, tipo):
    try:
      df = pd.read_csv(nome, encoding="latin1")
      return df.loc[df[coluna] == igual, tipo].item()
    except:
      return 0

  def preço_zerado(self, arquivo, destino, coluna="preco", igual=0, coluna_retorno="codigo"):
    
    df = pd.read_csv("csv/dados_das_cotações.csv", encoding="latin1")

    df[coluna] = df[coluna].str.replace("R\$", "", regex=True).str.replace(",", ".").str.replace('"', "").astype(float)

    ativo_zerado = df.loc[df[coluna] == igual, coluna_retorno]

    for valor in ativo_zerado:
        self.escrever_csv(nome=destino, conteudo=valor, tipo="a", separador=",")

  def Ticker(self, tipo):
    df = pd.read_csv("csv/url.csv", encoding="latin1")

    ticker = df.loc[df["tipo"] == f" {tipo}", "codigo"]
    return ticker
  def url(self, tipo):
    df = pd.read_csv("csv/url.csv", encoding="latin1")
    ticker = df.loc[df["tipo"] == f" {tipo}", "url"]
    return ticker
class moeda:
  def __init__(self):
    pass

  def formatar_moeda(self, valor):
    moeda = str(valor)
    if len(valor) > 20:
      moeda = str(valor).replace(".", ",")
      virgula = moeda.find(",")
      ponto = "."
      repartir = virgula - 3
      return "R$" + moeda[:repartir] + ponto + moeda[repartir:]
    
    else:
      return moeda
    
if __name__ == "__main__":
  tempo = Tempo()
  print(tempo.Dias_da_semana(True))
