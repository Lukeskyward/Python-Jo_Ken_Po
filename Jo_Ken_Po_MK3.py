from random import choice
from time import sleep
from colorama import init, Fore


init()


def draw(x, y):
    if x == item[0] and y == 0 or x == item[1] and y == 1 or x == item[2] and y == 2:
        return Fore.CYAN + "EMPATE!" + Fore.RESET


print("-=" * 15)
print("\n         JO KEN PO!\n")
print("-=" * 15)

again = 1
while again == 1:
    item = ('Pedra', 'Papel', 'Tesoura')
    computer = choice(item)
    print('\n\nSuas opções:\n\n'
          '[0] Pedra\n'
          '[1] Papel\n'
          '[2] Tesoura')

    player = 3
    while player > 2:
        try:
            player = int(input('\nQual é a sua jogada? '))
            if player > 2:
                print(Fore.RED + '\nJOGADA INVÁLIDA!' + Fore.RESET)
        except ValueError:
            print(Fore.RED + '\nJOGADA INVÁLIDA!' + Fore.RESET)
            player = 3

    sleep(0.3)
    print("\nJO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO!\n")
    print("-=" * 15)
    print(f"O jogador escolheu {item[player]}")
    print(f"O computador escolheu {computer}")
    print("-=" * 15, "\n")

    draw(computer, player)

    if (computer == item[0] and player == 1 or computer == item[1] and
            player == 2 or computer == item[2] and player == 0):
        print(Fore.GREEN + "O JOGADOR VENCEU!" + Fore.RESET)
    elif (computer == item[0] and player == 2 or computer == item[1] and
            player == 0 or computer == item[2] and player == 1):
        print(Fore.YELLOW + "O COMPUTADOR VENCEU!" + Fore.RESET)

    again = 3
    while again > 1:
        try:
            again = int(input("\nJogar novamente? 1 - Sim / 0 - Não: "))
            if again > 1:
                print(Fore.RED + '\nOPÇÃO INVÁLIDA!' + Fore.RESET)
        except ValueError:
            print(Fore.RED + '\nOPÇÃO INVÁLIDA!' + Fore.RESET)
            again = 3
