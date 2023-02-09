#def soma(numero1, numero2):
#    resp = numero1 + numero2
#    return resp
#retorno = soma (12.35,75.6)
#print(retorno)

#def tem_sete_itens(argum):
#    if len(argum) == 7:
#        return True
#    else:
#        return False
#a = [1,2,3,4]
#print(tem_sete_itens(a))
colecao = [1,24,56,2011,3,4]
def maior_num(x):
    maior = x[0]
    for n in x:
        if n > maior:
            maior = n
    return maior
print(maior_num(colecao))
