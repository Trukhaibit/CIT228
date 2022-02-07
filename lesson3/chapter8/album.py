def make_album(artist,albumTitle,songs=0):
    if songs == 0:
        return {artist:albumTitle}
    else:
        return {f"{albumTitle} by {artist}":songs}
print(make_album("Weird Al Yankovic","Mandatory Fun"))
print(make_album("Parry Gripp","Parry Gripp Mega Party"))
print(make_album("Jonathan Coulton","Artificial Heart"))
print(make_album("Joe Hertler and the Rainbow Seekers","Paper Castle",12))
quit = ""
while quit != "q":
    name = input("Input artist name: ")
    title = input("Input album name: ")
    song = int(input("Input number of songs (type 0 to skip) "))
    print(make_album(name,title,song))
    quit = input("type anthing to continue, or type q to quit ")