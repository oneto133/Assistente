from main import AI
from dados_excel import main as excel
import asyncio
from iniciar_cotação import Programa
import threading
import os
from receber_email import listar_mensagens
from enviar_email import enviar_mensagem
def run_async(coroutine):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(coroutine)
    loop.close()

class assistente(AI, Programa):
    def __init__(self):
        super().__init__()
        self.stop_event = threading.Event()
        self.email()

    def Verificar_resposta(self, pergunta):
        ia = self.diálogo(pergunta)
        try:
            if ia[0] == "low":
                resposta = self.responder(pergunta=ia[1], arquivo=r"pkl/comandos_ia.pkl")
                print(resposta[0])
                valor = self.executar(str(resposta[0]))
                enviar_mensagem(titulo=ia[1], mensagem=resposta, mensagem_final=valor)
        except:
            pass
    def email(self):
        usuario = ""
        while True:
            mensagem = listar_mensagens()
            if mensagem == None:
                continue
            if mensagem != usuario:
                self.Verificar_resposta(mensagem)
                usuario = mensagem
                print(usuario)

    def Guardar_historico(self, usuário, ia):
        with open("csv/erros.csv", "a") as file:
            file.write(f"usuário:  {usuário}, IA: {ia}")

    def Responder(self):
        pass
    
    def executar(self, função):
        nome_funçao = função
        try:
            funcao = getattr(self, nome_funçao) #Chama a função dentro da classe
            if callable(funcao):
                valor = funcao()
                return valor
            else:
                return "função não encontrada..."
        except AttributeError:
            return "Nenhuma função resposta"

    def dados_excel(self):
        excel()
        return "Executado, verifique seu onedrive"       

    def encerrar(self):
        return "Encerrando o programa...", os._exit(0)
        

    def cotação(self):
        thread = threading.Thread(target=run_async, args=(self.main(),))
        thread.start()
        return "Inicio de obtenção de dados de cotação..."

if __name__ == "__main__":
    assistente() 