name = input("Howdy partner, what's your name? ")
print("Howdy " + name + (" How about we give you a good cowboy name"))
surname = input("What's your surname? ")

#default cowboy name, if no other can be worked out.
new_name = "Ranger"
new_surname = "Cassidy"

if len(name) > 0:
    name_starting_char = name.lower()[0]
    if name_starting_char == "a": new_name = "Butch"
    elif name_starting_char == "b": new_name = "Prospector"
    elif name_starting_char == "c": new_name = "Dakota"
    elif name_starting_char == "d": new_name = "Bearcat"
    elif name_starting_char == "f": new_name = "Smokey"
    elif name_starting_char == "g": new_name = "Hunter"
    elif name_starting_char == "h": new_name = "Cactus"
    elif name_starting_char == "i": new_name = "Buckey"
    elif name_starting_char == "j": new_name = "Tanner"
    elif name_starting_char == "k": new_name = "Redwood"
    elif name_starting_char == "l": new_name = "Rattlesnake"
    elif name_starting_char == "m": new_name = "Hickory"
    elif name_starting_char == "n": new_name = "Outlaw"
    elif name_starting_char == "o": new_name = "Woody"
    elif name_starting_char == "p": new_name = "Mustang"
    elif name_starting_char == "q": new_name = "Stallion"
    elif name_starting_char == "r": new_name = "Casey"
    elif name_starting_char == "s": new_name = "Wrangler"
    elif name_starting_char == "t": new_name = "Rider"
    elif name_starting_char == "u": new_name = "Texas"
    elif name_starting_char == "v": new_name = "Deputy"
    elif name_starting_char == "w": new_name = "Slick"
    elif name_starting_char == "x": new_name = "Colt"
    elif name_starting_char == "y": new_name = "Lone"
    elif name_starting_char == "z": new_name = "Cash"

if len(surname) > 0:
    surname_starting_char = surname.lower()[0]
    if surname_starting_char == "a": new_surname = "Sundance"
    elif surname_starting_char == "b": new_surname = "Leather"
    elif surname_starting_char == "c": new_surname = "Tumbleweed"
    elif surname_starting_char == "d": new_surname = "Two Guns"
    elif surname_starting_char == "f": new_surname = "Lawless"
    elif surname_starting_char == "g": new_surname = "Nimbleboots"
    elif surname_starting_char == "h": new_surname = "Frosty"
    elif surname_starting_char == "i": new_surname = "Rocky"
    elif surname_starting_char == "j": new_surname = "Bullstep"
    elif surname_starting_char == "k": new_surname = "Mad Dog"
    elif surname_starting_char == "l": new_surname = "Bronco"
    elif surname_starting_char == "m": new_surname = "Bucky"
    elif surname_starting_char == "n": new_surname = "Deadwood"
    elif surname_starting_char == "o": new_surname = "Sunset"
    elif surname_starting_char == "p": new_surname = "Flint"
    elif surname_starting_char == "q": new_surname = "Whirlwind"
    elif surname_starting_char == "r": new_surname = "Quickshot"
    elif surname_starting_char == "s": new_surname = "Mcgee"
    elif surname_starting_char == "t": new_surname = "Eagle"
    elif surname_starting_char == "u": new_surname = "Cotton"
    elif surname_starting_char == "v": new_surname = "Gold Teeth"
    elif surname_starting_char == "w": new_surname = "Wild Hog"
    elif surname_starting_char == "x": new_surname = "Sly Eye"
    elif surname_starting_char == "y": new_surname = "Fast Draw"
    elif surname_starting_char == "z": new_surname = "Sharpshooter"

print("You're new name is " + new_name  + " " + new_surname)
