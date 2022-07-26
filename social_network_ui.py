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
    print("4. Unblock user. ")
    print("5. Send a message")
    print("6. View all my friends")
    print("7. View all my messages")
    print("8. View blocked users")
    print("9. <- Go back ")
    return input("Please Choose a number: ")

def editDetailsMenu():
        print("")
        print("1. Edit username")
        print("2. Edit password")
        print("3. Edit both")
        print("4. <- Go back")

def loginToAccount(users):
    global username #these are necessary for class functions to work (taken as arguments in main social_network file)
    global password
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users.keys(): #checks if username exists
        for k,v in users.items(): #cycles through every key-value pair, checks if that password is correct
            if password == v[0]:
                return manageAccountMenu()
    else: #username does not exist
        print("Username incorrect. ")
        return False
    
    print("Password not found. ")
    return False

#reads files
def readUsers():
    try:
        with open('userData.json', 'r+') as f: #opens file, sets to read and write
            return json.load(f) #returns a dictionary of the json data
    except: #if the file doesnt exist, it will be created
        return {} 

#writes to files to save users
def writeUsers(users):
    with open("userData.json", "w+") as f: #opens file, sets to read and write
        json.dump(users, f, indent=4) #dumps modified data back into json file, rewriting it
#view messages functions
def viewMessages():
    users = readUsers()
    print("")
    print("Your messages are:", users[username][2]) #just prints out the message list

#view friend function
def viewFriends():
    users = readUsers()
    print("")
    print("Your friends list:",users[username][1]) #just prints out the friend list
#view friend function
def viewBlockedUsers():
    users = readUsers()
    print("")
    print("Your blocked users list:",users[username][3]) #same as before