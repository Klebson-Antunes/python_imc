
def calcula_imc():
    altura = input("Digite sua altura: ")
    peso = input("Digite seu peso: ")
    altura = altura.replace(',', '.')
    peso = peso.replace(',', '.')
    imc = float(peso) / pow(float(altura), 2)
    return imc

def classificacao_imc(imc):
    classificacao = ["Magreza", "Normal", "Sobrepeso", "Obesidade grau I", "Obesidade grau II", "Obesidade grau III"]
    
    imc_real = [imc <= 18.5, imc >= 18.6 and imc <= 24.9, imc >= 25 and imc <=29.9, imc >= 30 and imc <= 34.9, imc >= 35 and imc <= 39.9, imc >= 40]
    
    for classifica in range(0, len(classificacao)):
        if(imc_real[classifica]):
            return classificacao[classifica]
        
def imc():
    inicio = """
    *****************
    *****Calcular IMC
    *****************
    """
    print(inicio)
    
    imc = calcula_imc()
    classificacao = classificacao_imc(imc)
    print("Seu imc é {} e esta com {}.".format(format(imc, '.2f'), classificacao))

if(__name__ == "__main__"):
    imc()


