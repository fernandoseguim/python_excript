num = int(input("Informe um numero: "))

result = "par" if num % 2 == 0 else "impar"

mensagem = "O número informado, foi o número %d e ele é \"%s\"" % (num, result)

print(mensagem)
