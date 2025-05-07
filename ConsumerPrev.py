print('Bem vindo ao ConsumerPrev! \nInsira seus equipamentos eletrônicos juntamente com o consumo indicado na etiqueta\ndo Inmetro.\n')
print('-'*35)
 
import time
 
def linhas():
    print('-'*50)
    print('')
    return None
 
def aparelhos_data(watt,horas):
    consumo = watt*horas
    return consumo
dicionario = {}
#print("Digite os dados dos seus equipamentos eletrônicos: \n")
def aparelhos_dados():
    time.sleep(0.5)
    nome = input("Nome do equipamento: \n")
    time.sleep(0.3)
    watt = float(input('Consumo KWh/mês: \n'))
    time.sleep(0.3)
    horas = float(input("Horas de uso por dia: \n"))
    time.sleep(0.3)
    consumo = watt*horas
    dicionario[nome] = consumo
    return consumo
 
aparelhos_dados()
linhas()
 
while True:
    deseja_adicionar = input("Deseja adicionar outro equipamento?\nS/N\n")
    linhas()
    time.sleep(0.5)
    if deseja_adicionar == 'S':
        aparelhos_dados()
        linhas()
    elif deseja_adicionar == 'N':
        break
    else:
        time.sleep(0.5)
        print("Opção inválida! Por favor, responda com 'S' ou 'N'.\n")
        linhas()
 
print(dicionario)
 
soma_valores = sum(dicionario.values())
print("Seu consumo mensal aproximado é de:")
time.sleep(2.0)
print(soma_valores,'Kwh')