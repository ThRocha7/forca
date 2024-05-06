# print('-----------')
# print('|         0')
# print('|       / | \ ')
# print("|        / \ ")
# print('|')
# forca = {
#     'cima': '----------',
#     'meio': '|',
#     'baixo': '|'
# }

# for i in forca:
#     print(forca[i])
# ei = input()

# if ei == '1':
#     forca['meio'] += '        0'

# for i in forca:
#     print(forca[i])
# print('-----------')


# print('|         ')
# print('|        ')
# print("|         ")
# print('|')

# def pao(ei, op):
#     if ei not in op:
#         op = op.append(ei)

    
# opa = []
# ei = input('teste > ')
# key = 'labio'

# while ei != 'ok':
#     if ei in key:
#         po = pao(ei, opa)
#         ei = input('teste > ')   
#     else: 
#         print('não ta')
#         ei = input('teste > ')
# print(opa)

# def soma(ei):
#     ei += 1 
#     return ei

# ei = 0

# pao = soma(ei)

# print(ei)

# key = 'apa'
# ei = input()

# if ei in key:
#     print(key.index(ei))

ei = input()
key = 'tomou'
posicoes = []
tamanho = len(key)
escondido = ['_']*tamanho
print(''.join(escondido))

for i in range(len(key)):
    if key[i] == ei:
        posicoes.append(i)
print(posicoes)

if ei in key:
    for posicao in posicoes:
        escondido[posicao] = ei
print(''.join(escondido))

# forca = {
#     'nv': ''.join(['-']*3)
# }

# print(forca)