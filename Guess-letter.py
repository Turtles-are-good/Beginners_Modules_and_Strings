import random
num = int(random.randint(1, 26))
tries = 0
if num == 1 :
    letter = "a"
elif num == 2 :
    letter = "b"
elif num == 3 :
    letter = "c"
elif num == 4 :
    letter = "d"
elif num == 5 :
    letter = "e"
elif num == 6 :
    letter = "f"
elif num == 7 :
    letter = "g"
elif num == 8 :
    letter = "h"
elif num == 9 :
    letter = "i"
elif num == 10 :
    letter = "j"
elif num == 11 :
    letter = "k"
elif num == 12 :
    letter = "l"
elif num == 13 :
    letter = "m"
elif num == 14 :
    letter = "n"
elif num == 15 :
    letter = "o"
elif num == 16 :
    letter = "p"
elif num == 17 :
    letter = "q"
elif num == 18 :
    letter = "r"
elif num == 19 :
    letter = "s"
elif num == 20 :
    letter = "t"
elif num == 21 :
    letter = "u"
elif num == 22 :
    letter = "v"
elif num == 23 :
    letter = "w"
elif num == 24 :
    letter = "x"
elif num == 25 :
    letter = "y"
elif num == 26 :
    letter = "z"
print(f"(For checker's sake, the letter is: {letter})")
while True :
    user = input("Guess the letter: \n").lower()
    tries += 1
    if user == letter :
        print("Correct letter")
        break
print(f"The letter is {letter} and you took {tries} tries.")