user = "Apratim"
password = "12345"

def login():
    print("Enter User & Password")
    entry1 = input("User Name:")
    entry2 = input("Password:")
    if entry1 == user and entry2 == password:
        print("Login Successful")
        logged_in()
    else:
        print("Login Failed")

def logged_in():
    print("Logged in")
    quit()

login()