import random
num = int(random.randint(1,100))
print(f"(For the marker's sake, the number is: {num})")
tries = 0
hi = True
print("guess the number")
while hi :
    user = input()
    if user.isdigit() :
        nums = int(user)
        tries += 1
        if nums == num :
            print("Correct number")
            hi = False
        elif nums > num :
            print("Your guess was too high")
        elif nums < num :
            print("Your guess was too low")
    else :
        print("Please enter a correct number")
print(f"The answer is {num} and you took {tries} tries to get it.")