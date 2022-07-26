import json
import social_network_ui
# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk

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
        users[self.id] = self.password, self.friendlist, self.messagelist
        social_network_ui.writeUsers(users)
        #print(type(users["username"]))

        Person(self.id, self.password)


class Person:
    #creates new user w/ two empty lists for messages and friends
    def __init__(self, name, password):
        self.id = name
        self.password = password
        self.friendlist = []
        self.messagelist = []

    def editDetails(): #really convoluted way of allowing users to edit account details
        result = input("Select action: ") 
        if result == "4": #had to put this if statement up here, i know its ugly
            return
        users = social_network_ui.readUsers()
        oldUser = input("Enter current username: ")
        oldPass = input("Enter current password: ")
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
            

    def add_friend(username):
        newFriend = input("Enter friend's username: ")
        users = social_network_ui.readUsers()
        if newFriend in users.keys():
            users[username][1].append(newFriend)
            #print(users)
            social_network_ui.writeUsers(users)
        else:
            print("User does not exist. ")
        #print(users)
        #print(type(users[username]))

    def send_message(username):
        global messageList
        messageList = []
        users = social_network_ui.readUsers()
        user = input("What user would you like to send the message to? ")
        if user in users.keys():
            message = input("What is your message: ")
            user[username][2].append(message)
        else:
            print("User does not exist. ")
            return
