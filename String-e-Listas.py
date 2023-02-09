frase = "Oi,tudo bem?"
lista_nomes = ['João','Maria','Guilherme','Diego']
lista_nomes.append("Carlinhos")
lista_nomes.append("Renatinha")
lista_nomes.remove("Guilherme")
lista_nomes.insert(1,"Jacinto")
lista_nomes[3] = "João"
contador_j = lista_nomes.count("João")

# lista_nomes.clear() <- limpa a lista toda

print(lista_nomes)
frase_separada = frase.split(",")
print(frase_separada)
