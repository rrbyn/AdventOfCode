import math

f= open("input.txt","r")
totalFuel = 0
addedFuel = 0

for x in f:
    addedFuel = (math.floor(int(x) / 3) - 2)
    totalFuel = addedFuel + totalFuel
    while addedFuel >= 0:
        addedFuel = (math.floor(int(addedFuel) / 3) - 2)
        if addedFuel >= 0:
            totalFuel = addedFuel + totalFuel
print (totalFuel)

