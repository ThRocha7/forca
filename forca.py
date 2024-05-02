
def pedir_jogada():
    jogada = input('Tente uma letra ou a palavra chave > ')
    return jogada

def verificador(tentativa):
    if tentativa == '':
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

def jogada_valida(tentativa, realizado_antes, keyword):
    if tentativa in keyWord:
        print()
    if tentativa in realizado_antes:
        print(f'A letra "{tentativa}" já foi tentada antes, tente novamente')
        print(realizado_antes)
    else:
        realizado_antes = realizado_antes.append(tentativa)
        
        print(realizado_antes)

keyWord = input('Digite a palavra chave > ')
continue_game = True
jogadas_realizdas = []

while continue_game == True:
    jogada = pedir_jogada()
    verificado = verificador(jogada)

    if verificado == False:
        print('Jogada inválida')
        jogada = pedir_jogada()
    elif verificado == 'Chute':
        continue_game = tentativa_keyword(jogada, keyWord, continue_game)
    elif verificado == True:
        jogada_validada = jogada_valida(jogada, jogadas_realizdas, keyWord)
    


