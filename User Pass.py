usernameInput = input("Username : ")
passInput = input("Password : ")
if usernameInput == "admin" and passInput == "1234":
    print("Succeed")
    print("Please select options")
    print("1.VAT Calculator")
    print("2.Price Calculator")
    userSelect = int(input(">>"))
    if userSelect == 1:
        price = int(input("Price (THB): "))
        vat = 7
        result = price + (price * vat / 100)
        vatr = (price * vat / 100)
        print("Price     =", price, "THB")
        print("VAT       =", vatr, "THB")
        print("Total     =", result, "THB")
    elif userSelect == 2:
        priceX = int(input("Enter price1 : "))
        priceY = int(input("Enter price2 : "))
        print(priceX + priceY)
else:
    print("Login Failed")