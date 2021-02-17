correctNum = 10
userGuess = 0
while userGuess != correctNum:
    userGuess = int(input("Put your number : "))
    if userGuess > correctNum:
        print("Too much")
    elif userGuess < correctNum:
        print("Too less")
    elif userGuess == correctNum:
        print("Correct!!")