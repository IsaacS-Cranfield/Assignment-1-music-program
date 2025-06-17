# Music app making use of lists and tuples
import time
import json
import sys
import getpass
import hashlib

# Create necessary files
open("users.json", "a").close()


''' Basic user structure:
username = {
    "email": "",
    "password": "",
    "playlists": [
        {
            "name": "",
            "songs": [
                ("title", "artist", "0:00"),
            ]
        },
        {
            "name": "",
            "songs": [
                ("title", "artist", "0:00")
            ]
        }
    ]
}
'''

# Example menu function
'''
def menu():
    while True:
        # Title
        delay()
        print("\n" + "=" * 40)
        print(f" Example Title ")
        print("=" * 40)
        delay()
        # Options
        delay(1)
        typewriter("1. Option 1", 0.05) # typewriter effect duration should be ajusted to the length of the text
        delay(0.2)
        typewriter("2. Option 2", 0.05)
        delay(0.2)
        typewriter("3. Option 3", 0.05)
        delay(0.5)

        choice = input("Enter an option (1-3): ").strip()
        delay()
        match choice:
            case "1":
                
            case "2":
                
            case "3":
'''                

# function for delay
def delay(seconds=0.5): # can use an argument, otherwise will default to 0.5 seconds
    time.sleep(seconds)

# Function to show a spinner for loading (pointless, but looks cool)
def spinner(seconds=2, text="Loading"): # just like the delay function, will default to 2 seconds with no argument
    # 'text' argument allows for custom text
    spin_chars = ['|', '/', '-', '\\']
    end_time = time.time() + seconds
    idx = 0
    while time.time() < end_time:
        print(f"\r{text}... {spin_chars[idx % len(spin_chars)]}", end='', flush=True)
        time.sleep(0.1)
        idx += 1
    print(f"\r{text}... Done!     ")
    delay(0.3) # Short delay after spinner 

def typewriter(text, delay_time=0.05):
    # Function to simulate typewriter effect for given text
    for char in text:
        print(char, end='')
        time.sleep(delay_time)  # Delay between each character
    print()  # New line after the text
   
# password hashing function 
def hash_password(password):
    # Using SHA-256 for hashing the password
    return hashlib.sha256(password.encode()).hexdigest()[:12]  # Truncate to 12 characters for simplicity




# ================
# MENU FUNCTIONS
# ================

# Main menu guest (not logged in)
def main_menu_guest():
    while True:
        # Title
        delay()
        print("\n" + "=" * 40)
        print("      Welcome to the Music Manager      ")
        print("=" * 40)
        delay()
        # Options
        delay(1)
        typewriter("1. User Login", 0.03)
        delay(0.2)
        typewriter("2. Create User Account", 0.02)
        delay(0.2)
        typewriter("3. Exit", 0.05)
        delay(0.5)
        
        choice = input("Enter an option (1-3): ").strip()
        delay()
        match choice:
            case "1":
                user_login()
                
            case "2":
                create_account()
                
            case "3":
                print("Exiting the application. Goodbye!")
                delay(1)
                sys.exit()

            case _:
                print("Invalid option. Please try again.")
    
def main_menu_user(username):
    while True:
        # Title
        delay()
        print("\n" + "=" * 40)
        print(f" {username}, Welcome to the Music Manager      ")
        print("=" * 40)
        delay()
        # Options
        delay(1)
        typewriter("1. Manage My Playlists", 0.02)
        delay(0.2)
        typewriter("2. Create Playlist", 0.03)
        delay(0.2)
        typewriter("3. Logout", 0.05)
        delay(0.5)

        choice = input("Enter an option (1-3): ").strip()
        delay()
        match choice:
            case "1":
                manage_playlists(username)
            case "2":
                delay()
                create_playlist(username)
            case "3":
                print(f"{username}, are you sure you want to log out?. ")
                delay()
                confirm = input("Enter 'yes' or 'no':  ").strip().lower()
                delay()
                if confirm == "yes":
                    print(f"Logging out {username}.")
                    delay(1)
                    main_menu_guest()
                else:
                    print("Logout cancelled. Returning to main menu.")
                    delay(1)
                    
def admin_menu():
    while True:
        # Title
        delay()
        print("\n" + "." * 40)
        print("      Admin Menu      ")
        print("." * 40)
        delay()

        # Show all users before options
        try:
            with open("users.json", "r") as f:
                users = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            users = {}

        if not users:
            print("No users available.")
        else:
            print("\nAll registered users:")
            for username, details in users.items():
                print(f"Username: {username}, Email: {details['email']}, Playlists: {len(details['playlists'])}")
            print()

        # Options
        delay(1)
        typewriter("1. Edit User", 0.03)
        delay(0.2)
        typewriter("2. Delete User", 0.02)
        delay(0.2)
        typewriter("3. Exit", 0.05)
        delay(0.5)

        choice = input("Enter an option (1-3): ").strip()
        delay()
        match choice:
            case "1":
                edit_user()  # Function to edit a user
            case "2":
                delete_user()  # Function to delete a user
            case "3":
                print("Exiting the admin menu.")
                delay(1)
                sys.exit()
            case _:
                print("Invalid option. Please try again.")


# ==========================             
# USER MANAGEMENT FUNCTIONS
# ==========================

# User account creation.
def create_account():
    while True:
        # Prompt user for details
        username = input("Enter a username: ").strip()

        # Propmt for email and validation
        while True:
            email = input("Enter your email: ").strip().lower()
            # Validate email format (basic validation)
            if "@" not in email or "." not in email:
                delay()
                print("Invalid email format. Please try again.")
                continue # return to start of the loop to re-enter email
            break

        while True:
            # Prompt for password
            password = getpass.getpass("Enter a password: ").strip() # getpass will hide the password input
            passconfirm = getpass.getpass("Confirm your password: ").strip() # confirm password
            # Check if passwords match
            if password != passconfirm: 
                delay()
                print("Passwords do not match. Please try again.")
                continue
            else:
                break
        hashed_password = hash_password(password) # save the hashed password instead of plain text

        while True:
            is_admin = input("Elevate to admin? (yes/no): ").strip().lower()

            if is_admin == "yes" or is_admin == "no":
                break
            
            else:
                delay()
                print("Invalid input. Please enter 'yes' or 'no'.")
                continue

        # Load all existing users from JSON
        try: # Try to read the users.json file
            with open("users.json", "r") as f:
                users = json.load(f)
        # If the file is empty or not found, initialize an empty dictionary
        except (json.JSONDecodeError, FileNotFoundError):
            users = {}

        # Check if username already exists
        if username in users:
            delay()
            print("Username already exists. Please choose another.")
            continue
        break
    
    # save new user details in the specified format
    users[username] = {
        "email": email,
        "password": hashed_password,
        "is_admin": is_admin == "yes",  # Convert to boolean
        "playlists": []
    }

    # Save the updated users back to JSON
    with open("users.json", "w") as f: # make sure to use write mode, not append
        json.dump(users, f, indent=4)

    spinner(text="Saving account details")
    print(f"Account created for {username} with email {email}.")
    delay(2)

# user login function.
def user_login():
    max_attempts = 3 # Maximum attempts for login
    attempts = 0 # Counter for login attempts

    # Load all existing users from JSON
    try:
        with open("users.json", "r") as f:
            users = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        users = {}

    while attempts < max_attempts:
        # Prompt for username and password
        username = input("Enter your username: ").strip()
        password = getpass.getpass("Enter your password: ").strip() # Hide the password input
        hashed_password = hash_password(password) # Hash password again for comparison

        # Check if username exists and password matches, and if the user is an admin or not
        # For non admin users:
        if username in users and users[username]["password"] == hashed_password and not users[username]["is_admin"]:
            spinner(0.5, text="Checking credentials") # Show spinner for 0.5 seconds
            spinner(2, text="Logging in") # Show longer spinner for login
            delay(1)
            main_menu_user(username)
        # For admin users:
        elif username in users and users[username]["password"] == hashed_password and users[username]["is_admin"]:
            spinner(0.5, text="Checking credentials") # Show spinner for 0.5 seconds
            spinner(2, text="Logging in") # Show longer spinner for login
            delay(1)
            admin_menu()  # Redirect to admin menu if user is an admin
        else: 
            delay()
            print("Invalid username or password. Please try again. ")
            delay()
            attempts += 1
            continue  # Continue to prompt for username and password
    # If max attempts reached, exit
    if attempts == max_attempts:
        print("Maximum login attempts reached. Exiting the application.")
        delay(1)
        sys.exit()

def view_all_users():
    # Load all existing users from JSON
    try:
        with open("users.json", "r") as f:
            users = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        print("No users found or users file is empty.")
        return

    if not users:
        print("No users available.")
        return

    print("\nAll registered users:")
    for username, details in users.items():
        print(f"Username: {username}, Email: {details['email']}, Playlists: {len(details['playlists'])}")
    input("Press Enter to continue...")  # Wait for user input before returning
    delay(1)

def edit_user():
    # Load all existing users from JSON
    try:
        with open("users.json", "r") as f:
            users = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        print("No users found or users file is empty.")
        return

    if not users:
        print("No users available to edit.")
        return

    print("\nAll registered users:")
    for idx, username in enumerate(users.keys(), 1):
        print(f"{idx}. {username}")
    
    try:
        user_index = int(input("Enter the index of the user to edit (1-based index): ")) - 1
        if 0 <= user_index < len(users):
            username_edit = list(users.keys())[user_index]
            new_email = input(f"Enter new email for '{username_edit}' (leave blank to keep current): ").strip()
            if new_email:
                users[username_edit]["email"] = new_email
                with open("users.json", "w") as f:
                    json.dump(users, f, indent=4)  # Save updated users back to JSON
                spinner(text="Updating user details")
                print(f"User '{username_edit}' updated successfully.")
            else:
                print("No changes made to the user's email.")
        else:
            print("Invalid user index. Please try again.")
    except ValueError:
        print("Please enter a valid number.")


def delete_user():
    # Load all existing users from JSON
    try:
        with open("users.json", "r") as f:
            users = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        delay()
        print("No users found or users file is empty.")
        delay(1)
        return

    if not users:
        delay()
        print("No users available to delete.")
        delay(1)
        return

    print("\nAll registered users:")
    delay()
    for idx, username in enumerate(users.keys(), 1):
        print(f"{idx}. {username}")
        delay(0.2)

    try:
        user_index = int(input("Enter the index of the user to delete (1-based index): ")) - 1
        delay()
        if 0 <= user_index < len(users):
            username_delete = list(users.keys())[user_index]
            confirm = input(f"Are you sure you want to delete '{username_delete}'? (yes/no): ").strip().lower()
            delay()
            if confirm == "yes":
                del users[username_delete]  # Delete the user from the dictionary
                with open("users.json", "w") as f:
                    json.dump(users, f, indent=4)  # Save updated users back to JSON
                spinner(text="Deleting user")
                print(f"User '{username_delete}' deleted successfully.")
                delay(1)
            else:
                print("User deletion cancelled.")
                delay(1)
        else:
            print("Invalid user index. Please try again.")
            delay(1)
    except ValueError:
        print("Please enter a valid number.")
        delay(1)


# =====================
# PLAYLIST MANAGEMENT
# =====================

# Function to enter the playlist management menu.
def manage_playlists(username):

    while True:
        # Title
        print("\n" + "/\\" * 10)
        print(f" Playlist management ")
        print("/\\" * 10)
        delay()

        playlists = view_playlists(username)  # Show all playlists for the user

        # Options
        delay()
        typewriter("1. Edit playlist", 0.03)
        delay(0.2)
        typewriter("2. Delete playlist", 0.03)
        delay(0.2)
        typewriter("3. Return to main menu", 0.02)
        delay(0.5)

        choice = input("Enter an option (1-3): ").strip()
        print("")
        delay()
        match choice:
            # Edit playlist
            case "1":
                #playlists = view_playlists(username)
                if not playlists:
                    print("No playlists available to edit.")
                    continue

                try:
                    # Prompt for playlist index to edit
                    playlist_index = int(input("Enter the index of the playlist to edit (1-based index): ")) - 1
                    delay()
                    edit_playlist(username, playlist_index)  # Call the edit function and pass username and playlist index
                except ValueError:
                    print("Please enter a valid number.")

            # Delete playlist
            case "2":
                spinner(1, text="Checking for playlists") # Show spinner for loading playlists
                # Load JSON containing user data

            # Return to the main menu
            case "3":
                print(f"Returning to main menu for {username}.")
                delay(1)
                main_menu_user(username)  # Return to the main user menu

            case _:
                print("Invalid option. Please try again.")

# function to create a new playlist
def create_playlist(username):
    # Load user data from JSON
    try:
        with open("users.json", "r") as f:
            users = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        users = {}

    if username not in users:
        print("User not found.")
        return

    # Prompt for playlist name
    playlist_name = input("Enter the name of the new playlist: ").strip()
    if not playlist_name:
        print("Playlist name cannot be empty.")
        return

    # Create new playlist structure
    new_playlist = {
        "name": playlist_name,
        "songs": []
    }

    # Add the new playlist to the user's playlists
    users[username]["playlists"].append(new_playlist)

    # Save updated user data back to JSON
    with open("users.json", "w") as f:
        json.dump(users, f, indent=4)

    spinner(text="Saving new playlist")

    print(f"Playlist '{playlist_name}' created successfully.")

# Function to return all loged in users playlists
def view_playlists(username):
    spinner(1, text="Checking for playlists")  # Show spinner for loading playlists
    # Load JSON containing user data
    try:
        with open("users.json", "r") as f:
            users = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        print("No playlists found.")
        return []

    playlists = users[username].get("playlists", [])
    if playlists:
        typewriter(f"\nPlaylists for {username}:", 0.02)
        for idx, playlist in enumerate(playlists, 1):
            print(f"{idx}. {playlist['name']} ({len(playlist['songs'])} songs)")
            delay()
        #input("Press Enter to continue...\n")  # Wait for user input before returning
        print()
        delay(1)
        return playlists
    else:
        print("You have no playlists yet.")
        delay(1)
        return []

# function to edit a playlist
def edit_playlist(username, playlist_index):
    try:
        with open("users.json", "r") as f:
            users = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        print("No playlists found or users file is empty.")
        return

    if username not in users:
        print ("User not found.")
        return
    
    playlists = users[username].get("playlists", [])

    if 0 <= playlist_index < len(playlists):
        playlist = playlists[playlist_index]

        while True:
            print("\n" + "~" * 30)
            print(f"Editing playlist: {playlist['name']}")
            print("~" * 30)

            # Show songs before options
            if not playlist["songs"]:
                print("No songs in the playlist.")
            else:
                typewriter("Songs in the playlist:", 0.02)
                for idx, song in enumerate(playlist["songs"], 1):
                    print(f"{idx}. {song[0]} by {song[1]} ({song[2]})")
                    delay()
            print()

            delay()
            # Options (no view songs option)
            typewriter("1. Edit playlist name", 0.03)
            delay(0.2)
            typewriter("2. Add song", 0.04)
            delay(0.2)
            typewriter("3. Remove song", 0.04)
            delay(0.2)
            typewriter("4. Back to playlist management", 0.02)

            choice = input("Enter an option (1-4): ").strip()
            print("")  # Print a new line for better readability
            delay()

            match choice:
                # Edit playlist name
                case "1":
                    new_name = input("Enter new playlist name: ").strip()
                    if new_name:
                        playlist["name"] = new_name
                        print(f"Playlist name changed to '{new_name}'.")
                        delay(1)
                    else:
                        print("Invalid playlist name. Please try again.")

                # Add song to playlist
                case "2":
                    add_song(username, playlist_index, playlist)

                # Remove song from playlist
                case "3":
                    remove_song(username, playlist_index, playlist)  # Call the remove song function

                # Back to playlist management
                case "4":
                    break
                case _:
                    print("Invalid option. Please try again.")

        # Save updated playlists back to JSON
        users[username]["playlists"] = playlists
        with open("users.json", "w") as f:
            json.dump(users, f, indent=4)

    else:
        print("Invalid playlist index. Please try again.")
        delay(1)
        return

# Function to delete a playlist
def delete_playlist(username, playlist_index):
    try:
        with open("users.json", "r") as f:
            users = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        users = {}

    if username not in users:
        return

    playlists = users[username].get("playlists", [])
    if 0 <= playlist_index < len(playlists):
        playlists.pop(playlist_index)
        users[username]["playlists"] = playlists
        with open("users.json", "w") as f:
            json.dump(users, f, indent=4)

# Function to add songs to a playlist
def add_song(username, playlist_index, playlist):
    # Load JSON containing user data
    try:
        with open("users.json", "r") as f:
            users = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        print("No playlists found or users file is empty.")
        return []
    
    song_title = input("Enter song title: ").strip()
    song_artist = input("Enter song artist: ").strip()
    song_duration = input("Enter song duration (e.g., 3:45): ").strip()
    if song_title and song_artist and song_duration:
        playlist["songs"].append((song_title, song_artist, song_duration))

        # Update user dictionary with the new song
        users[username]["playlists"][playlist_index] = playlist
        # Save updated playlists back to JSON
        with open("users.json", "w") as f:
            json.dump(users, f, indent=4)
        spinner(text="Adding song")
        print(f"Song '{song_title}' by {song_artist} added to the playlist.")
        delay(1)
    else:
        print("Invalid song details. Please try again.")

# Function to remove a song from a playlist
def remove_song(username, playlist_index, playlist):
    # Load JSON containing user data
    try:
        with open("users.json", "r") as f:
            users = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        print("No playlists found or users file is empty.")
        return []

    if not playlist["songs"]:
        delay()
        print("No songs in the playlist to remove.")
        delay(1)
        return
    print("\nSongs in the playlist:")
    delay()

    song_index = int(input("\nEnter the index of the song to remove (1-based index): ")) - 1
    if 0 <= song_index < len(playlist["songs"]):
        removed_song = playlist["songs"].pop(song_index)
        users[username]["playlists"][playlist_index]["songs"] = playlist["songs"]  # Update the songs in the playlist
        # Save updated playlists back to JSON
        with open("users.json", "w") as f:
            json.dump(users, f, indent=4)
        spinner(text="Removing song")
        delay(1)
        print(f"Removed '{removed_song[0]}' by {removed_song[1]} from the playlist.")
        delay(1)
    else:
        print("Invalid song index.")
   


# Program flow guide: 
'''
1. Start with the main menu for guests.
2. Allow guests to log in or create an account.
3. If logged in, show the main menu for users.
4. From the user menu, allow users to manage playlists, create new playlists, or log out.
5. In the playlist management menu, allow users to view, edit, or delete playlists.
'''

# ===============
# PROGRAM START
# ===============

main_menu_guest()  
