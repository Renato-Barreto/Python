""" Tipos de variáveis """

x = 'Renato'
y = 14
z = 2.3
w = True

""" Operações Matemáticas """
"""Média Aritmética"""
n1= 5.5
n2= 8.3
n3= 7.5

media = (n1+n2+n3)/3

"""Condicional If Else"""

if (media>=7):
    situacao = 'Aprovado'
elif (media >=3 and media < 7):
    situacao = 'em Recuperação'
else:
    situacao = 'Reprovado'

"""Template = Variáveis e Mensagens (f'conteúdo,{variável},conteúdo')"""
print(f'A sua média foi {media:.1f}, você está {situacao}')

""" Vetor """

x=[12,23,43,24,31,33,56,58]

x.append(121)
x.insert(3,45)
x.pop()
x.remove(43)

print(x)

#append() - inserir um novo valor na última posição do vetor
#insert() - inserir um novo valor em qualquer posição do vetor
#pop() - eliminar o valor da última posição do vetor // ou posição descrita
#remove() - eliminar pelo valor uma posição do vetor

""" Laço de repetição - FOR """

for camile in x:
    if (camile >= 30):
        print(camile)


#for <varredor> in <vetor>: --- laço de repetição "for"

""" Laço de repetição - FOR """

positivo=[]
negativo=[]

for varredor in x:
    if (varredor < 0):
        positivo.append(varredor)
    else:
        negativo.append(varredor)

print(positivo)
print(negativo)