def mostrar_forca(chave, tentativa, erros, visualizar): #vai printar a forca, os erros, acertos e as tentativas
    forca = {
        # 'espaco': '',
        # 'nv0': 'Já usado:',
        # 'espaco2': '',
        'nv1': '------------',
        'nv2': '|',
        'nv3': '|',
        'nv4': '|',
        'nv5': '|',
        'nv6': 'palavra chave:',
        'nv7':  modificar_nv7(chave, tentativa)
    }
    
    for i in forca:
        print(forca[i])

def modificar_nv7(chave, tentativa):
    posicoes = []
    visualizador_chave = ['_']*len(chave)
    
    if tentativa == '':
        return ''.join(visualizador_chave)
    
    elif tentativa in chave:
        for i in range(len(chave)):
            if chave[i] == tentativa:
                posicoes.append(i)
                visualizador_chave[i] = tentativa
    return ''.join(visualizador_chave)
         

def pedir_jogada():
    jogada = input('Tente uma letra ou a palavra chave > ').upper()
    return jogada

def verificador(tentativa):
    if tentativa == '' or type(tentativa) != str:
        return False
    else: return True
        
def tentativa_final(tentativa, keyword, continuar):
    if tentativa == keyword:
        print("Acertou!")
        return False
    else: 
        print("Errou tente novamente")
        return True

def caminho_tentativa(tentativa, realizadas, certas, chave, errado):
    if len(tentativa) > 1:
        return 'final'
    else:
        if tentativa not in realizadas:
            realizadas = realizadas.append(tentativa)
        else: print('Já foi jogado')
        
        if tentativa in chave:
            if tentativa not in certas:
                certas = certas.append(tentativa)
            return 'certo'
        else: return 'errado'

keyWord = input('Digite a palavra chave > ').upper()
continue_game = True
jogadas_realizadas = []
jogadas_certas = []
jogada = ''
erros = 0
visualizador_chave = ['_']*len(keyWord)

while continue_game == True:
    mostrar_forca(keyWord, jogada, erros, visualizador_chave)
    jogada = pedir_jogada()
    verificado = verificador(jogada)
    if verificado == False:
        print('Jogada inválida')
    else: 
        tentativa = caminho_tentativa(jogada, jogadas_realizadas, jogadas_certas, keyWord, erros)
        if tentativa == 'final':
            continue_game = tentativa_final(jogada, keyWord, continue_game)
        # else:
        #     mostrar(tentativa, jogadas_certas)
            
    


