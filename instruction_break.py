print("Início da execução do laço")
i = 0
while(i < 10):
    i = i + 1
    if (i % 2 == 0):
        continue
    print("o número %d é impar" %i)
else:
    print("else")



print("fim da execução laço")