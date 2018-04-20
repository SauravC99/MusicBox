import musicbox

my_music = musicbox.MusicBox()

#These are all of the constant global lists we need
NOTE_LETTERS = ["C", "D", "E", "F", "G", "A", "B"]
NOTE_NUMBERS = [60, 62, 64, 65, 67, 69, 71]
MAJOR_SCALE_INTERVALS = [2, 2, 1, 2, 2, 2, 1]
MINOR_SCALE_INTERVALS = [2, 1, 2, 2, 1, 2, 2]


def note_to_int(note):
    #Adjusts the integer of the note for # or b
    #Change is set to 0 so it wont effect anything is # or b is not included
    change = 0
    if note[1:] == "#":
        change = 1
    if note[1:] == "b":
        change = -1
    #Validates that the note is in the correct format
    if len(note) > 1 and (note[1:] != "#" and note[1:] != "b"):
        return -1
    for i in range(len(NOTE_LETTERS)):
        #If the inputed note is found in the list, it will return it
        if NOTE_LETTERS[i] == note[:1]:
            #The + change is for if the user put a # or a b
            return NOTE_NUMBERS[i] + change
    #Returns -1 if note is not valid
    return -1

#Broken 4/2/18
#Fixed 4/3/18
#Broken again 4/5/18
#Fixed method and made it more efficient 4/6/18
def note_to_scale(note, type):
    #Makes a new list
    notes = []
    #If the scale is minor, change values according to minor list and append to notes
    if type == "minor":
        #Adds the first note to list
        notes.append(note)
        for i in MINOR_SCALE_INTERVALS:
            #Adds and apends
            note += i
            notes.append(note)
    #If the scale is major, change values according to major list and append to notes
    if type == "major":
        #Adds the first note to list
        notes.append(note)
        for i in MAJOR_SCALE_INTERVALS:
            #Adds and apends
            note += i
            notes.append(note)
    #Return the list
    return notes

#Prints the main menu
def print_menu():
    print("Main Menu:")
    print("1. Play Notes")
    print("2. Play Scale")
    print("3. Quit")

#Validates user's menu choice, between 1 and 3
def get_menu_choice():
    ch = int(input("Please enter a selection: \n"))
    while ch > 3 or ch < 1:
        ch = int(input("Please enter a selection: \n"))
    return ch

#Ask user for notes and validate
def get_notes():
    notes = input("Please enter a sequence of notes separated by spaces: \n")
    a = notes.split(" ")
    ints = []
    for i in range(len(a)):
        #If the note is not invalid, add it to list
        if note_to_int(a[i]) != -1:
            ints.append(note_to_int(a[i]))
    return ints

#Uses a loop to play notes
def play_notes(notes):
    for i in notes:
        my_music.play_note(i, 500)

#Make sure there are notes to play
def menu_play_notes():
    n = get_notes()
    #If none of the notes are recognized, print error
    if len(n) == 0:
        print("I don't know any of these notes.")
    else:
        play_notes(n)

#Validation deoesn't work 3/30/18
#Fixed 4/3/18
#Ask the user for a scale and validate it
def get_scale():
    scale = input("Please enter a scale name (Ex. C major): \n")
    #Splits to get each part
    sc = scale.split(" ")
    #If the user only puts in "B" instead of "B major", append a space
    #Into the list so the program won't crash
    if len(sc) == 1:
        sc.append(" ")
    #FIXME Validation doesn't work all the time
    #FIXED
    #Validates scale to make sure its in the right format and corect note
    while ((sc[1] != "minor" and sc[1] != "major") or note_to_int(sc[0]) == -1):
        #Does the steps again so program will work as intended
        scale = input("Please enter a scale name (Ex C major): \n")
        sc = scale.split(" ")
        if len(sc) == 1:
            sc.append(" ")
    return scale

#Uses a loop to play every note in scale
def play_scale(scale):
    for i in scale:
        #Plays for 500 milliseconds, 1/2 second
        my_music.play_note(i, 500)

#Play scale method, gets information about the scale,
#Makes the scale and plays it
def menu_play_scale():
    scale_str = get_scale()
    scale_list = scale_str.split(" ")
    note = note_to_int(scale_list[0])
    scale_int = note_to_scale(note, scale_list[1])
    play_scale(scale_int)

#Main method, runs the respective methods for the user's choice
def main():
    while True:
        print_menu()
        menu = get_menu_choice()
        if menu == 3:
            break
        if menu == 1:
            menu_play_notes()
        if menu == 2:
            menu_play_scale()
        print("")

main()

my_music.close()