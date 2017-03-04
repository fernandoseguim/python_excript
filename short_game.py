from random import randint

hit = False;
machine_number = randint(1,9)
shot_number = -1
attemps_numbers = 0

while (shot_number != machine_number):
    shot_number = int(input("Dê um novo palpite: "))

    attemps_numbers += 1
    if shot_number == 0:
        print("Jogo interrompido!")
        break
    elif (shot_number == machine_number):
        print("PARABÉNS você acertou após %d tentativas " % attemps_numbers)

    elif (shot_number < machine_number):
        print("Você ainda não acertou, tente um número maior ou digite 0 para sair!")
    else:
        print("Você ainda não acertou, tente um número menor ou digite 0 para sair!")
else:
    print("Fim do jogo!")



