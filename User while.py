usernameInput = input("Username : ")
passInput = input("Password : ")
while usernameInput != "admin" or passInput != "1234":
    print("Failed, Try again")
    usernameInput = input("User : ")
    passInput = input("Password : ")
    print("Succeed")