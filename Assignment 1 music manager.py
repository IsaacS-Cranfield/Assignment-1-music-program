# Music app making use of lists and tuples
import time

# Create necessary files
open("users.json", "a").close()

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

      
