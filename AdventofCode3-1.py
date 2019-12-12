f= open("input3.txt","r")
counter = 0
currentPos = [0,0]

for x in f:
    movementPath = (x.split(","))

def movementEngine(counter):

    # tee teise wirei loop ja võrdle currentpos
    for m in movementPath:
        if movementPath[counter][0] == "R":
             currentPos[1] = currentPos[1] + int(movementPath[counter][1] + movementPath[counter][2])
             counter = counter + 1
        elif movementPath[counter][0] == "L":
            currentPos[1] = currentPos[1] - int(movementPath[counter][1] + movementPath[counter][2])
            counter = counter + 1
        elif movementPath[counter][0] == "U":
            currentPos[0] = currentPos[0] + int(movementPath[counter][1] + movementPath[counter][2])
            counter = counter + 1
        elif movementPath[counter][0] == "D":
            currentPos[0] = currentPos[0] - int(movementPath[counter][1] + movementPath[counter][2])
            counter = counter + 1

movementEngine(counter)

print (currentPos)

