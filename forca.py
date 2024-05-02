
def pedir_jogada():
    jogada = input('Tente uma letra ou a palavra chave > ').upper()
    return jogada

def verificador(tentativa):
    if tentativa == '' or type(tentativa) != str:
        validado = False
        return validado
    elif len(tentativa) > 1:
        validado = 'Chute'
        return validado
    else: 
        validado = True
        return validado
        
def tentativa_keyword(tentativa, keyword, continuar):
    if tentativa == keyword:
        print("Acertou!")
        continuar = False
        return continuar
    else: 
        print("Errou tente novamente")
        continuar = True
        return continuar

def tentativa_letra(tentativa, realizado_ant, chave, certas):
    if tentativa in chave:
        realizado_ant = realizado_ant.append(tentativa)
        certas = certas.append(tentativa)
        print(realizado_ant)
        print(certas)



keyWord = input('Digite a palavra chave > ').upper()
continue_game = True
realizado_antes = []
letras_certas = []

while continue_game == True:
    jogada = pedir_jogada()
    verificado = verificador(jogada)
    if verificado == False:
        print('Jogada inválida')
    elif verificado == 'Chute':
        continue_game = tentativa_keyword(jogada, keyWord, continue_game)
    elif verificado == True:
        jogada_validada = tentativa_letra(jogada, realizado_antes, keyWord, letras_certas)
    


