#Acumulador
Acumulador = 0
#Lista para guardar info
Lista_de_Info = []

#
f = open("./Dados/amazon.csv", "r")
if f:
    for linha in f:
        Lista_de_Info = linha.split(",")
        if Lista_de_Info[0] == "2010" and Lista_de_Info[1] == '"Santa Catarina"':
            Acumulador += 1
        else:
            pass
    f.close()
else:
    print("Nenhum arquivo encontrado")
print(Lista_de_Info[0])
print(Lista_de_Info)

print(f"O número total de incêndios ocorridos em Santa Catarina no ano de 2010 foi de {Acumulador}")