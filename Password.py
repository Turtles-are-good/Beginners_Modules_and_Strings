password = input("Enter a password: \n").strip()
score = 0
hi = int(len(password))
hehe = 0
hihi = 0
if hi > 7 :
    score += 1
if password.islower() == False :
    score += 1
if password.isupper() == False :
    score += 1
if any(char.isdigit() for char in password) :
    hehe += 1
    if hehe >= 1 :
        score += 1
if any(not i.isalnum() for i in password) :
        score += 1
if score == 5 :
    print("Your password is strong")
elif score == 4 or score == 3 :
    print("Your password is moderately strong")
elif score == 2 or score == 1 or score == 0 :
    print("Your password is weak")