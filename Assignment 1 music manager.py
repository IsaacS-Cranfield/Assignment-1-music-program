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
   
# password hashing function 
def hash_password(password):
    # Using SHA-256 for hashing the password
    return hashlib.sha256(password.encode()).hexdigest()[:12]  # Truncate to 12 characters for simplicity

# Main menu guest (not logged in)
def main_menu_guest():
    while True:
        # Title
        time.sleep(0.5)
        print("\n")
        print("=" * 40)
        print("      Welcome to My Music Manager      ")
        print("=" * 40)

        # Options
        time.sleep(1)
        print("1. User Login")
        print("2. Create User Account")
        print("3. Exit")

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

        # Prompt for password
        password = getpass.getpass("Enter a password: ").strip() # getpass will hide the password input
        hashed_password = hash_password(password) # save the hashed password instead of plain text

        # Load all existing users from JSON
        try:
            with open("users.json", "r") as f:
                users = json.load(f)
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
    while True:
        # Prompt for username and password
        username = input("Enter your username: ").strip()
        password = getpass.getpass("Enter your password: ").strip() # Hide the password input
        hashed_password = hash_password(password) # Hash password again for comparison

        # Load all existing users from JSON
        try:
            with open("users.json", "r") as f:
                users = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            users = {}

        max_attempts = 3 # Maximum attempts for login
        attempts = 0 # Counter for login attempts
        while attempts < max_attempts:
            # Check if username exists and password matches
            if username in users and users[username]["password"] == hashed_password:
                spinner(0.5, text="Checking credentials") # Show spinner for 0.5 seconds
                delay(0.3) # Short delay for effect
                spinner(2, text="Logging in") # Show longer spinner for login
                delay(0.3)
                print(f"Login successful for {username}.")
                delay(2)
                return username
            else: 
                delay()
                print("Invalid username or password. Please try again. ")
                delay()
                attempts += 1
        # If max attempts reached, exit
        if attempts == max_attempts:
            print("Maximum login attempts reached. Exiting the application.")
            delay(1)
            sys.exit()



'''
# Function to print the playlist to the user.
def print_playlist(playlist):
    time.sleep(0.5)
    print("Welcome to the Music App!")
    time.sleep(0.5)
    print("Playlist: ")
    for song in playlist:
        # Print details of each song in the playlist with string formatting.
        print(f"Title: {song[0]}, Artist: {song[1]}, Duration: {song[2]}")

# 3. Function to add a song to the playlist.
def add_song(playlist):
    # .strip and .lower to remvoe spaces and convert to lowercase.
    title = input("Enter the song title: ").strip().lower()
    artist = input("Enter the artist: ").strip().lower()
    duration = input("Enter the duration: ").strip()
    playlist.append((title, artist, duration))
    time.sleep(0.5)
    print(f"Added {title} by {artist} to the playlist.")
    
# 4. Function to remoev a song in the playlist.
def remove_song(playlist):
    time.sleep(0.5)
    title = input("Enter the title of the song to remove: ").strip().lower()
    playlist = [song for song in playlist if song[0] != title]
'''

main_menu_guest()  
