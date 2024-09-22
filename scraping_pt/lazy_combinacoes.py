letras = ['c', 'f', 'e', 'i', 't', 'o', 'n']

print(len(letras))
combinacoes = []

for j in range(0, 7):
    for k in range(0, 7):
        for l in range(0, 7):
            for m in range(0, 7):
                for n in range(0, 7):
                    for o in range(0, 7):
                        for p in range(0, 7):
                            temp = []
                            temp.append(letras[j])
                            temp.append(letras[k])
                            temp.append(letras[l])
                            temp.append(letras[m])
                            temp.append(letras[n])
                            temp.append(letras[o])
                            temp.append(letras[p])
                            combinacoes.append(temp)

print(len(combinacoes))
for c in combinacoes:
    print(''.join(c))
    print("\n")


with open("combinacoes.txt", "w") as file:
    for c in combinacoes:
        file.write(''.join(c) + "\n")