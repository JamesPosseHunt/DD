from random import randint

def d4():
    result = randint(1, 4)
    return result

def d6():
    result = randint(1, 6)
    return result

def d8():
    result = randint(1, 8)
    return result

def d10():
    result = randint(1, 10)
    return result

def d12():
    result = randint(1, 12)
    return result

def d20():
    result = randint(1, 20)
    return result

def menu():
    print("Choose Dice to Roll: ")
    print("D4 (Press 4), D6 (Press 6), D8 (Press 8)")
    print("D10 (Press 10), D12 (Press 12), D20 (Press 20)")
    print("Exit (Press 0)")


result = 0
menu()
choice = int(input("Choice: "))
while choice != 0:
    if choice == 4:
        print(d4())
    elif choice == 6:
        print(d6())
    elif choice == 8:
        print(d8())
    elif choice == 10:
        print(d10())
    elif choice == 12:
        print(d12())
    elif choice == 20:
        print(d20())
    else:
        print("Error: Invalid option. Try again.")
    menu()
    choice = int(input("Choice: "))
