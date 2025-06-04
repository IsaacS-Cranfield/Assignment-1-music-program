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
def delay(seconds=0.5): # does not require an argument. if 
    time.sleep(seconds)
   
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
                print("Login functionality not implemented yet.")
                
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
    # Prompt user for details
    username = input("Enter a username: ").strip()
    email = input("Enter your email: ").strip().lower()
    # Validate email format (basic validation)
    if "@" not in email or "." not in email:
        print("Invalid email format. Please try again.")
        return
    password = getpass.getpass("Enter a password: ").strip() # getpass will hide the password input
    hashed_password = hash_password(password) # save the hashed password instead of plain text

    # Here you would typically save the user details to a file or database.
    # For now, we will just print them.
    print(f"Account created for {username} with email {email}.")
    print(f"Hashed password: {hashed_password}")
    delay(2)


#user login function.
#def user_login():


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
