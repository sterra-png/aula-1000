numero_tuple = (1,2,3,4,5) #numero da tuple

numero_list = list(numero_tuple) #trasformaçao do tuple para liste
print(numero_list)

numero_list.extend([12,8]) #colocar 2 indices no final da lista
print(numero_list)

numero_list.pop () #remover o utimo indice da lista
print(numero_list)

print(numero_list[0]) #aparece o primeiro indice

print(len(numero_list)) #quantidade de indices na lista

dicionario = { #criaçao do dicionario
    'nome': 'felipe',
    'idade': 17,
    'profição': 'QA',
}
print(dicionario['nome']) #apresentar apenas o nome no dicionario