f= open("input43.txt","r")
floor = 0


for str(x) in f:
    print (x)
    if x == "(":
        floor = floor + 1
    elif x == ")":
        floor = floor - 1

print (floor)