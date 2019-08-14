# CH8 Exercise 8-7 and 8-8
#
# album.py
#
# Exercise 8-7
# Write a function called make_album() that builds a dictionary describing
# a music album

def make_album(artist_name, album_title, number_of_tracks=''):

    album = {
        'artist': artist_name.title(),
        'album title': album_title.title(),
    }

    # Check for number of tracks
    if number_of_tracks:
        album['number of tracks'] = number_of_tracks

    return album

# Call dictionary function three times
print(make_album('korn', 'untouchables'))
print(make_album('tech n9ne', 'sickology 101'))
print(make_album('disturbed', 'the sickness'))

# number_of_tracks is stored as integer in dictionary
eminem = make_album('eminem', 'encore', 10)
print(eminem)


# Exercise 8-8
# Write a while loop that prompts users for artist and album title
# Call make_album() and print dictionary.  Use 'q' as quit condition
while True:
    print("\nEnter the name of an artist.  ")
    print("Press 'q' any time to quit.  ")

    artist = input("Artist: ")
    if artist == 'q':
        break

    album = input("Album: ")
    if album == 'q':
        break

    print(make_album(artist, album))
