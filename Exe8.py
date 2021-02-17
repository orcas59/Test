usernameInput = input("Username : ")
passInput = input("Password : ")
if usernameInput == "admin" and passInput == "1234":
    print("Welcome To Shop")
    print("Please select product")
    print("1.Apple  :",10)
    print("2.Banana :",20)
    print("3.Orange :",15)
    select = int(input(">> "))
    if select == 1:
        amountX = int(input("Enter amount : "))
        applePrice = 10
        print("Apple x", amountX, "=", amountX * applePrice,"THB")
    elif select == 2:
        amountX = int(input("Enter amount : "))
        bananaPrice = 20
        print("Banana x", amountX, "=", amountX * bananaPrice,"THB")
    elif select == 3:
        amountX = int(input("Enter amount : "))
        oragnePrice = 15
        print("Orange x", amountX, "=", amountX * oragnePrice,"THB")
    elif select >= 4:
        select = int(input("Wrong number, Select again >> "))
        if select == 1:
            amountX = int(input("Enter amount : "))
            applePrice = 10
            print("Apple x", amountX, "=", amountX * applePrice, "THB")
        elif select == 2:
            amountX = int(input("Enter amount : "))
            bananaPrice = 20
            print("Banana x", amountX, "=", amountX * bananaPrice, "THB")
        elif select == 3:
            amountX = int(input("Enter amount : "))
            oragnePrice = 15
            print("Orange x", amountX, "=", amountX * oragnePrice, "THB")
else :
    print("Login failed")