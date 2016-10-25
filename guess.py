import random

num = random.randint(0, 100)

while True:
    try:
        guess = int(input("Enter 1 ~ 100: "))
    except ValueError as e:
        print ("Please enter number 1 ~ 100:")
        continue
    if guess > num:
        print ("guess Bigger:")
    elif guess < num:
        print ("guess Smaller:")
    else:
        print ("Guess OK, Game Over")
        break
    print ("\n")
