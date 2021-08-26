
import random


def Kazanova():
    ver = 0
    while (ver == 0):
        player = int(input("1 - kamień, 2 - nożyce, 3 - papier. "))
        if (player == 1 or player == 2 or player == 3):
            ver = 1
    if player == 1:
        print("Ty wybrałesz Kamień")
    if player == 2:
        print("Ty wybrałesz Nożyce.")
    if player == 3:
        print("Ty wybrałeś Papier.")
    comp = random.randint(1, 3)
    if comp == 1:
        print("Komputer wybrał Kamień.")
    if comp == 2:
        print("Komputer wybrał Nożyce.")
    if comp == 3:
        print("Kmputer wybrał Papier.")

    # Kto wygrał
    if player == comp:
        win = 0
    elif player == 1 and comp == 2 or player == 2 and comp == 3 or player == 3 and comp == 1:
        win = 1
    # elif player == 1 and comp == 3 or player == 2 and comp == 1 or player == 3 and comp == 2:
        #win = 2
    else:  # player == 3 and comp == 2:
        win = 2

    if win == 0:
        print("Nikt Nie wygrał")
    elif win == 1:
        print("Wygrał player!")
    else:  # win == 2:
        print("Wygrał komputer!")


if __name__ == "__main__":
    while True:
        Kazanova()
        odpowiedz = input("Gramy Dalej? N=koniec: ")
        if odpowiedz == 'N' or odpowiedz == 'n':
            break
