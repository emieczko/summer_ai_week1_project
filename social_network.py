#Various import Statements can go here
from numpy import inner
from  social_network_classes import SocialNetwork,Person
import social_network_ui
#Create instance of main social network object
ai_social_network = SocialNetwork()

#The line below is a python keyword to specify which 
if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    choice = social_network_ui.mainMenu()

    while True: 
        if choice == "1":
            print("\nYou are now in the create account menu")
            ai_social_network.create_account()

        elif choice == "2":
            inner_menu_choice = social_network_ui.loginToAccount(social_network_ui.readUsers())
            if inner_menu_choice != 0:
                while True: #disgustingly large amount of if statements
                    if inner_menu_choice == "1":
                        social_network_ui.editDetailsMenu(social_network_ui.username)
                        Person.editDetails()
                    if inner_menu_choice == "2":
                        Person.add_friend(social_network_ui.username)
                    if inner_menu_choice == "3":
                        Person.blockUser(social_network_ui.username)
                    if inner_menu_choice == "4":
                        Person.unblockUser(social_network_ui.username)
                    if inner_menu_choice == "5":
                        Person.send_message(social_network_ui.username)
                    if inner_menu_choice == "6":
                        social_network_ui.viewFriends()
                    if inner_menu_choice == "7":
                        social_network_ui.viewMessages()
                    if inner_menu_choice == "8":
                        social_network_ui.viewBlockedUsers()
                    if inner_menu_choice == "9":
                        break
                    else:
                        inner_menu_choice = social_network_ui.manageAccountMenu()

        elif choice == "3":
            print("Thank you for visiting. Goodbye!")
            break

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()



        
