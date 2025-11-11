import os
import time
file_path = "players.txt"
import render

new_user = ""

username_loop = True

while username_loop:

    if new_user == "":
        # default operation if user prompts registration from the main menu.
        username = input("Input (Case Sensitive): ").strip()
    else: # Registration QoL: if user prompts during registration if the input username does not exists.
        username = new_user # to skip username input since it is already provided on the login function call

    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            player_found = False
            for line in file:
                if not line.strip():
                    continue
                _ , stored_user, _ = line.strip().split(",")
                if stored_user == username: # to consider case-senitive username storing
                    player_found = True
                    player_exists = f"Player with username '{username}' already exists."
                    render.menu_ui("custom",0,["USER REGISTRATION",player_exists])
                    while True:
                        choice = input("Do you want to log in instead? (yes/no?) ").strip()
                        if choice == "yes":
                            # return login(username) # proceed to login module
                            username_loop = False
                            break
                        elif choice == "no":                        
                            print("Please try a different username.")
                            time.sleep(1)
                            username = ""
                            username_loop = True
                            break
                        else:
                            print("Invalid Input!")
                    break
                # no action for unique username
            if not player_found:
                username_loop = False