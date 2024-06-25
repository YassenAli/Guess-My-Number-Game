import random
print("====================\nGuess My Number Game\n====================")
computer = random.randint(1, 100)
player = 0
tries = 0
while player != computer:
    player = int(input("Please enter your guess number : "))
    tries += 1
    if player > computer:
        print("Too high, try again.")
    elif player < computer:
        print("Too low, try again.")
    else:
        print(f"Congratulations!!!\nCorrect guess, you got it in {tries} tries.")
