def mostrar_forca(chave, tentativa):
    forca = {
    'nv1': '------------',
    'nv2': '|',
    'nv3': '|',
    'nv4': '|',
    'nv5': '|',
    'nv6': 'palavra chave: '
    }
    
    if tentativa == '':
        forca['nv6'] += ''.join(['_']*len(chave))
    else: forca['nv6'] = modificar_nv6(chave, forca, tentativa)

    for i in forca:
        print(forca[i])

def modificar_nv6(chave, forca, tentativa):
    posicoes = []
    qntd_letras = len(chave)
    
    if tentativa in chave:
        for i in range(len(chave)):
            if chave[i] == tentativa:
                posicoes.append(i)
    # for posicao in posicoes:
    #     for 
# def mostrar(tentativa, certas):
#     if tentativa == 'certo':
#         # print(f'A letra {tentativa} está certa. {certas}')
#     elif tentativa == 'errado':
#         print(f'A letra {tentativa} não faz parte da palavra chave')
    
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

def caminho_tentativa(tentativa, realizadas, certas, chave):
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

while continue_game == True:
    mostrar_forca(keyWord, jogada)
    jogada = pedir_jogada()
    verificado = verificador(jogada)
    if verificado == False:
        print('Jogada inválida')
    else: 
        tentativa = caminho_tentativa(jogada, jogadas_realizadas, jogadas_certas, keyWord)
        if tentativa == 'final':
            continue_game = tentativa_final(jogada, keyWord, continue_game)
        # else:
        #     mostrar(tentativa, jogadas_certas)
            
    


