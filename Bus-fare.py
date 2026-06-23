s = input("What number stop are you at? \n")
if s.isdigit() :
    start = int(s)
    f = input("What number stop do you want to arrive at? \n")
    if f.isdigit() :
        finish = int(f)
        print(f"The bus fare from stop {start} to stop {finish} is ${5 + (2.5 * (finish - start))}")
    else :
        print("Please enter a correct stop")
else :
    print("Please enter a correct stop")