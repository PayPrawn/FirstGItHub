#finds any 4 character password with each character having a Dec value between 48-57, 65-90, 97-122
#this means each password place 1st, 2nd, 3rd and 4th has 52 possible values, meaning the password has 62^4 combinations. 

import time
import math
passreal = "aaab"
start_time = time.time()

def ascii2(integer_value_entered):
    global valuemover
    global returned_value

    valuemover = integer_value_entered
    if valuemover == 1: 
        returned_value = "a"
    elif valuemover == 2:
        returned_value = "b"
    elif valuemover == 3:
        returned_value = "c"
    elif valuemover == 4:
        returned_value = "d"
    elif valuemover == 5:
        returned_value = "e"   
    elif valuemover == 6:
        returned_value = "f"
    elif valuemover == 7:
        returned_value = "g" 
    elif valuemover == 8:
        returned_value = "h"
    elif valuemover == 9:
        returned_value = "i"
    elif valuemover == 10:
        returned_value = "j"
    elif valuemover == 11:
        returned_value = "k"
    elif valuemover == 12:
        returned_value = "l"
    elif valuemover == 13:
        returned_value = "m"
    elif valuemover == 14:
        returned_value = "n"
    elif valuemover == 15:
        returned_value = "o"
    elif valuemover == 16:
        returned_value = "p"
    elif valuemover == 17:
        returned_value = "q"
    elif valuemover == 18:
        returned_value = "r"
    elif valuemover == 19:
        returned_value = "s"
    elif valuemover == 20:
        returned_value = "t"
    elif valuemover == 21:
        returned_value = "u"
    elif valuemover == 22:
        returned_value = "v"
    elif valuemover == 23:
        returned_value = "w"
    elif valuemover == 24:
        returned_value = "x"
    elif valuemover == 25:
        returned_value = "y"
    elif valuemover == 26:
        returned_value = "z"
    elif valuemover == 27:
        returned_value = "A"
    elif valuemover == 28:
        returned_value = "B"
    elif valuemover == 29:
        returned_value = "C"
    elif valuemover == 30:
        returned_value = "D"
    elif valuemover == 31:
        returned_value = "E"
    elif valuemover == 32:
        returned_value = "F"
    elif valuemover == 33:
        returned_value = "G"
    elif valuemover == 34:
        returned_value = "H"
    elif valuemover == 35:
        returned_value = "I"
    elif valuemover == 36:
        returned_value = "J"
    elif valuemover == 37:
        returned_value = "K"
    elif valuemover == 38:
        returned_value = "L"
    elif valuemover == 39:
        returned_value = "M"
    elif valuemover == 40:
        returned_value = "N"
    elif valuemover == 41:
        returned_value = "O"
    elif valuemover == 42:
        returned_value = "P"
    elif valuemover == 43:
        returned_value = "Q"
    elif valuemover == 44:
        returned_value = "R"
    elif valuemover == 45:
        returned_value = "S"
    elif valuemover == 46:
        returned_value = "T"
    elif valuemover == 47:
        returned_value = "U"
    elif valuemover == 48:
        returned_value = "V"
    elif valuemover == 49:
        returned_value = "W"
    elif valuemover == 50:
        returned_value = "X"
    elif valuemover == 51:
        returned_value = "Y"
    elif valuemover == 52:
        returned_value = "Z"
    elif valuemover == 53:
        returned_value = "0"
    elif valuemover == 54:
        returned_value = "1"
    elif valuemover == 55:
        returned_value = "2"
    elif valuemover == 56:
        returned_value = "3"
    elif valuemover == 57:
        returned_value = "4"
    elif valuemover == 58:
        returned_value = "5"
    elif valuemover == 59:
        returned_value = "6"
    elif valuemover == 60:
        returned_value = "7"
    elif valuemover == 61:
        returned_value = "8"
    elif valuemover == 62:
        returned_value = "9"

    return(returned_value)

def crack():
    y = 0
    x = 0
    z = 0
    w = 0
    for f in range(62**4):
        if y == 62: 
            y = 0
        if x == 3844:
            x = 0
        if z == 238328:
            z = 0
        place2floored = (math.floor(x / 62) + 1)
        place3floored = (math.floor(z / 3844) + 1)
        place4floored = (math.floor(w / 238328) + 1)
        place1 = ascii2((y + 1))
        place2 = ascii2(place2floored)
        place3 = ascii2(place3floored)
        place4 = ascii2(place4floored)
        passwordtry = place1 + place2 + place3 + place4
        x = x + 1
        y = y + 1
        z = z + 1
        w = w + 1
        if passwordtry == passreal:
            print("password is " + passwordtry)
            print("[runtime] " + (str(time.time() - start_time)) + "s")
            break

crack()
qanda = input("were you happy with the program ")
if qanda == "y":
    print("I am glad.")
elif qanda == "n":
    print("I am sorry to hear that.")
else:
    print("please enter only 'y' or 'n'")