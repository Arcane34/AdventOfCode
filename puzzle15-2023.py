data = []
boxes = []
for i in range(256):
    boxes.append([])

with open("puz15.txt") as file:
    for line in file:
        line = line.strip()
        data = line.split(",")
        
        
def instruction(x):
    lens = -1
    if "=" in x:
        label = x[:x.index("=")]
        lens = x[len(x)-1]
    else:
        label = x[:len(x)-1]
    boxNum = hash1(label,0)
    return [label, lens, boxNum]

def execute(ins, boxL):
    
    if ins[1] != -1:
        found = False
        curBox = boxL[ins[2]]
        for y in range(len(curBox)-1,-1,-1):
            if curBox[y][0] == ins[0]:
                found = True
                boxL[ins[2]][y][1] = ins[1]
        
        if not(found):
            boxL[ins[2]].append([ins[0], ins[1]])
        
    else:
        curBox = boxL[ins[2]]
        for y in range(len(curBox)-1,-1,-1):
            if curBox[y][0] == ins[0]:
                boxL[ins[2]].pop(y)


def focusingPow(boxesL):
    totalPow = 0
    for box in range(len(boxesL)):
        num1 = box+1
        for eLens in range(len(boxesL[box])):
            print((num1)*(eLens+1)*int(boxesL[box][eLens][1]), "   FOCUS POWER", num1, (eLens+1), int(boxesL[box][eLens][1]))
            totalPow += (num1)*(eLens+1)*int(boxesL[box][eLens][1])
    print(totalPow)




def hash1(text, cur):
    for j in text:
        cur += ord(j)
        cur *= 17
        cur = cur % 256
    return cur



total = 0
for j in data:
   execute(instruction(j), boxes)

for i in boxes:
    print(i)

focusingPow(boxes)

