f= open("input2.txt","r")
counter = 0
for x in f:
    opcode = (x.split(",","\n"))
    opcode = list(map(int, opcode))
    print (opcode[counter])
    print (opcode)
for x in opcode:
    if  opcode[counter] == 1:
        opcode[opcode[counter + 3]] = opcode[opcode[counter + 1]] + opcode[opcode[counter + 2]]
        counter = counter + 4
    elif opcode[counter] == 2:
        opcode[opcode[counter + 3]] = opcode [counter + 1] * opcode[counter + 2]
        counter = counter + 4
    elif opcode[counter] == 99:
        print ("found 99")
        break
    else:
        print ("error")
print (opcode)