f= open("input3.txt","r")
counter = 0
currentPoswire1 = [0,0]
currentPoswire2 = [0,0]
movementPath = []
lines = f.readlines()

wire1Path = (lines[0].split(","))
wire2Path = (lines[1].split(","))
wire1Path[-1] = wire1Path[-1].strip()

def movementEngine(counter, movementPath):

    # tee teise wirei loop ja võrdle currentpos
    for m in wire1Path and wire2Path:
        movementRequiredwire1 = int(wire1Path[counter][1] + wire1Path[counter][2])
        movementRequiredwire2 = int(wire2Path[counter][1] + wire2Path[counter][2])
        if wire1Path[counter][0] == "R":
            while movementRequiredwire1 != currentPoswire1:
                currentPoswire1[0] = currentPoswire1[0] + 1
            if wire2Path[counter][0] == "R":
                while movementRequiredwire2 != currentPoswire2:
                    currentPoswire2[0] = currentPoswire2[0] + 1
            elif wire2Path[counter][0] == "L":
                while movementRequiredwire2 != currentPoswire2:
                    currentPoswire2[0] = currentPoswire2[0] - 1

        


