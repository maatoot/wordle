import random
# adding 365 word 

sword_list = ["SNAKE","OCEAN","SHAME","SHOES","SHAKE",]
sword = random.choice(sword_list)


bg_yellow = "\u001b[43m"
bg_green = "\u001b[42m"
Reset = "\u001b[0m"

check = 0
for retry in range(6):
    try:
        guess = input("input your guess: ").upper()
        for i in range(5):
            if guess[i] == sword[i]:
                print(f"{bg_green}{guess[i]}{Reset}",end="")
            elif guess[i] in sword[i]:
                print(f"{bg_yellow}{guess[i]}{Reset}",end="")
            else:
                print(f"{guess[i]}",end="")
        print()
        if guess == sword:
            check = 1
            print(" You Win !!!")
            break
    except IndexError:
        print(f" The Word must be 5 chars")

if check == 1:
    print(f"You lose, the word was  {sword} ")

