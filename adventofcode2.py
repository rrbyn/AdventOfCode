f= open("input2.txt","r")
counter = 0

for x in f:
    opcode = (x.split(","))
    for x in opcode[counter:(counter + 4)]:
        if opcode[counter] == 1:
            opcode [counter + 3] = opcode[counter + 1] + opcode [counter + 2]
        elif opcode[counter] == 2:
            opcode [counter + 3] = opcode [counter + 1] * opcode[counter + 3]
print (opcode)    