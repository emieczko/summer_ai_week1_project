import json
# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
class SocialNetwork:
    def __init__(self):
        self.list_of_people = [] # this instance variable is initialized to an empty list when social network is created, 
                                 # you can save objects of people on the network in this list
        
    ## For more challenge try this
    def save_social_media(self):
        f = open('userData.json')

        data = json.load(f)
        for i in data:
            for user in self.list_of_people:
                if i == user:
                    break
                else:
                    json.dumps(user)
        # function to save social media to a file on disk 
        # hint: look up how to use python's inbuil json module to turn objects to json
        # you can write this json unto a file on disk
        pass

    ## For more challenge try this
    def reload_social_media(self):
        # function to load saved social media from file on disk 
        # hint: load a the json file from disk and look up how to recreate the list of people objects.
        pass

    def  create_account(self):
        self.id = input("Enter username: ")
        self.year = ("Enter age: ")
        #implement function that creates account here
        print("Creating ...")
        self.list_of_people.append(self.id)
        pass


class Person:
    def __init__(self, name, age, messages):
        self.id = name
        self.year = age
        self.friendlist = []
        self.messagelist = []

    def add_friend(self, person_object):
        self.friendlist.append(person_object)
        #implement adding friend. Hint add to self.friendlist
        pass

    def send_message(self):
        user = input("What user would you like to send the message to? ")
        #if user in userData.json:
        #   msg = input("Enter message you wish to send: ")
        #   add message to other user's message list
        #else:
        #   print("User does not exist. ") 
        #implement sending message to friend here
        pass
