my_number = 6
user_guess = input("what is your guess: ")
if not user_guess:
    print("enter a number")
    exit()
if user_guess >0:
    if user_guess == my_number:
        print("you win")
    elif user_guess >4 and user_guess < 8:
        print("you are colse")
    else:
        print("you lost")
else:
    print("enter a positive number")           