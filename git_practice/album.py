def make_album():
    """Return a dictionary of information about an album"""
    album_list = []
    while True:
        print("Answer each question to fill the album information. " + 
                    "Enter 'q' anytime to quit.")
        
        # statements prompting user input for album information
        artist_name = input("Enter the artist name:\n")
        if artist_name == 'q':
            break
        album_title = input("Enter the album title:\n")
        if album_title == 'q':
            break
        num_of_songs = input("Enter the number of songs in the album. " + 
                            "Press enter to omit this option.")
        if num_of_songs == 'q':
            break

        # generating dictionary of album information and adding to list album_list
        album_info = {}
        album_info['artist'] = artist_name
        album_info['album'] = album_title
        album_list.append(album_info)
    return album_list