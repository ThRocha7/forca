# print('-----------')
# print('|         0')
# print('|       / | \ ')
# print("|        / \ ")
# print('|')

# print('-----------')
# print('|         ')
# print('|        ')
# print("|         ")
# print('|')

def pao(ei, op):
    if ei not in op:
        op = op.append(ei)

    

ei = input('teste > ')
key = 'labio'
opa = []

while ei != 'ok':
    if ei in key:
        po = pao(ei, opa)
        ei = input('teste > ')  
        print(opa)
    else: print('não ta')





