#prompt user for name
name = input("What is your name? \n")

# database containing names of users who are allowed to use system
allowed_users = ["James", "Mary", "Fatu", "Joy"]

# default password for each user
allowed_password = "Password"

# check if the name the user enter is a valid name from the database
if(name in allowed_users):
    #prompt user to enter password
    password = input("Enter your password \n")

    # check if the password is correct 
    if(password == allowed_password):
        print("Welcome")

else:
    print("Username is not correct, try again");



