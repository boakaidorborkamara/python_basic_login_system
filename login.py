name = input("What is your name? \n")
allowed_users = ["James", "Mary", "Fatu", "Joy"]
allowed_password = "Password"

if(name in allowed_users):
    password = input("Enter your password \n")

    if(password == allowed_password):
        print("Welcome")

else:
    print("Username is not correct, try again");



