
# Decorators como funções (sintaxe não recomendada)

def seja_educado(funcao):
    def sendo():
        print("Foi um prazer conhecer você!")
        funcao()
        print("Tenha um otimo dia!")
    return sendo

def saudacao():
    print("Seja bem-vindo(a) à Geek University!")

teste = seja_educado(saudacao)
teste()

@seja_educado
def raiva():
    print("VÁ SE LASCAR!")

raiva()
    
