numero_tuple = (1,2,3,4,5)

numero_list = list(numero_tuple)
print('transformaçao do tuple'+ numero_list)

numero_list.extend([12,8])
print(numero_list)

numero_list.pop ()
print(numero_list)

print(numero_list[0])

print(len(numero_list))

dicionario = {
    'nome': 'felipe',
    'idade': 17,
    'profição': 'QA',
}
print(dicionario['nome'])