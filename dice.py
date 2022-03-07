from random import randint

while True:
    while True:
        c1=input("\nWhich dice?\n1-Normal\n2-Biased\nChoose: ")
        if c1=='1' or c1=='2':
            break
        print("Please enter a valid choice.")
    if c1=='1':
        dice = randint(1,6)
        
    else:
        while True:
            c2=int(input("Which number should the dice be biased towards?[1,2,3,4,5,6]\nChoose: "))
            if c2 in range(1,7):
                break
            print("Please enter a valid choice.")
        d1=randint(1,6)
        d2=randint(1,2)
        if d2==1:
            dice=d1
        else:
            dice=c2
    print("\nRolling dice...\n")
    print(dice)  
    con=input("\nDo you wish to continue?[Y/N]: ").upper()
    if con=='N':
        break

