# You can implement user interface functions here.
import json

def mainMenu():
    print("")
    print("1. Create a new account")
    print("2. Login to account")
    print("3. Quit")
    print("********************************************************")
    return input("Please Choose a number: ")

def manageAccountMenu():
    print("")
    print("1. Edit my details")
    print("2. Add a friend")
    print("3. Block user")
    print("4. Send a message")
    print("5. View all my friends")
    print("6. View all my messages")
    print("7. <- Go back ")
    return input("Please Choose a number: ")

def editDetailsMenu():
        print("")
        print("1. Edit username")
        print("2. Edit password")
        print("3. Edit both")
        print("4. <- Go back")

def loginToAccount(users):
    global username
    global password
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users.keys():
        for k,v in users.items():
            if password == v[0]:
                return manageAccountMenu()
    else:
        print("Username not found. ")
        return False
    
    print("Password not found. ")
    return False

#reads files
def readUsers():
    try:
        with open('userData.json', 'r+') as f:
            return json.load(f)
    except: #if the file doesnt exist, it will be created
        return {} 

#writes to files to save users
def writeUsers(users):
    with open("userData.json", "w+") as f:
        json.dump(users, f, indent=4)

def viewMessages():
    users = readUsers()
    print("")
    print("Your messages are:", users[username][2])

def viewFriends():
    users = readUsers()
    print("")
    print("Your friends list:",users[username][1])