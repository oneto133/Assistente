from main import AI
from dados_excel import main as excel

class assistente(AI):
    def __init__(self):
        super().__init__()
        self.Verificar_resposta()

    def Verificar_resposta(self):
        ia = self.diálogo()
        try:
            if ia[0] == "low":
                resposta = self.responder(pergunta=ia[1], arquivo=r"pkl/comandos_ia.pkl")
                print(resposta[0])
                self.executar(str(resposta[0]))
        except:
            pass

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
                funcao()
            else:
                print("função não encontrada...")
        except AttributeError:
            print("Nenhuma função resposta")

    def dados_excel(self):
        excel()
        print("executado")

if __name__ == "__main__":
    assistente()