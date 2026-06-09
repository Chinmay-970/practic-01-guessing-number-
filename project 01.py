import random
target = random.randint(1 , 100)
while True:
    userchoice = input("GUESS THE TARGET : OR QUIT :")
    if(userchoice == "quit"):
        break
    userchoice = int(userchoice)
    if(userchoice == target):
        print("successed : correct guess :")
        break
    elif(userchoice < target):
        print("your number was small , guess big :")
    else:
        print("your number was big , guess small :")
print("-----GAME OVER -----")