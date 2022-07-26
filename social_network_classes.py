#import json
import social_network_ui
# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
#you'll see random commented-out print statements from testing, please ignore them

class SocialNetwork:
    def __init__(self):
        self.list_of_people = [] # this instance variable is initialized to an empty list when social network is created, 
                                 # you can save objects of people on the network in this list

    def create_account(self): #create account function
        self.id = input("Enter username: ")
        self.password = input("Enter password: ")
        print("Creating ...")

        users = social_network_ui.readUsers() 
        self.friendlist = []
        self.messagelist = []
        self.blackList = []
        users[self.id] = self.password, self.friendlist, self.messagelist, self.blackList
        social_network_ui.writeUsers(users)
        #print(type(users["username"]))

        Person(self.id, self.password)


class Person:
    #creates new user w/ three empty lists for messages, friends, and blocked users
    def __init__(self, name, password):
        self.id = name
        self.password = password
        self.friendlist = []
        self.messagelist = []
        self.blackList = []

    def editDetails(): #really convoluted way of allowing users to edit account details
        result = input("Select action: ") 
        if result == "4": #had to put this if statement up here, i know its ugly
            return
        users = social_network_ui.readUsers()
        oldUser = input("Enter current username: ")
        #oldPass = input("Enter current password: ") #realized this is useless
        if result == "1": #this is for changing just the user; it just adds a new key-value pair to the dict, with a new name for the key
            newUser = input("Enter new username: ")
            users[newUser] = users.pop(oldUser)
            social_network_ui.writeUsers(users)
        elif result == "2": #new changing new password, just rewrites the value for password
            newPass = input("Enter new password: ")
            users[oldUser] = newPass, [], []
            social_network_ui.writeUsers(users)
        elif result == "3": #for changing both, creates a completely new key-value pair with a new rewritten value
            newUser = input("Enter new username: ")
            newPass = input("Enter new password: ")
            users[newUser] = users.pop(oldUser)
            users[newUser] = newPass, [], []
            social_network_ui.writeUsers(users)
        else: #failsafe
            print("Unknown choice. ")
            
    #add friend function
    def add_friend(username):
        newFriend = input("Enter friend's username: ")
        users = social_network_ui.readUsers()
        if newFriend in users.keys(): #checks if the user exists, and adds them to the friends list
            if newFriend in users[username][1]: #friend already exists
                return print("This user is already a friend. ")
            if username in users[newFriend][3]:
                return print("This user has blocked you.")
            users[username][1].append(newFriend)
            #print(users)
            social_network_ui.writeUsers(users)
            if newFriend in users[username][3]: #checks if the user is in the blacklist, and removes sthem
                users[username][3].remove(newFriend)
                social_network_ui.writeUsers(users)
        else: #failsafe
            print("User does not exist. ")
        #print(users)
        #print(type(users[username]))

    #send message function
    def send_message(username):
        #global messageList #i dont think i need these global variables
        #global sender
        #messageList = []
        users = social_network_ui.readUsers()
        user = input("What user would you like to send the message to? ")
        if user in users.keys(): #checks if user exists
            for k,v in users.items(): #cycles through every key-value pair, finding the correct user
                if k == user:         #once correct user is found, gets message and adds it to other user's message list
                    #sender = username
                    if username in users[user][3]:
                        return print("This user has blocked you. ")
                    elif username in users[username][3]:
                        return print("You must unblock this user first.")
                    message = input("What is your message: ")
                    #print(users[user][2])
                    totalMessage = "(From: " + username + ") " + message
                    #print(totalMessage)
                    users[user][2].append(totalMessage)
                    social_network_ui.writeUsers(users)
                else: #failsafe
                    continue
        else: #failsafe
            print("User does not exist. ")
            return
    
    #block user function
    def blockUser(username):
        #global userBlackList #pretty sure i dont need this
        #userBlackList = [] 
        badUser = input("What user would you like to block? ")
        users = social_network_ui.readUsers()
        if badUser in users.keys(): #checks if user exists
            if badUser not in users[username][3]: #checks if user is not already blocked, and if so, blocks them
                users[username][3].append(badUser)
                social_network_ui.writeUsers(users)
                #print(users[username][1])
                if badUser in users[username][1]: #checks if user is a friend, and if so, removes them
                    users[username][1].remove(badUser)
                    social_network_ui.writeUsers(users)
            else: #failsafe
                print("User is already blocked. ")
        else: #failsafe
            print("User does not exist. ")
    
    #unblock function, does the exact opposite of the block function
    def unblockUser(username):
        goodUser = input("What user would you like to unblock? ")
        users = social_network_ui.readUsers()
        if goodUser in users.keys():
            if goodUser in users[username][3]:
                users[username][3].remove(goodUser)
                social_network_ui.writeUsers(users)
            else:
                print("User is not blocked.")
        else:
            print("User does not exist. ")
