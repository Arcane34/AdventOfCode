data = []

with open("puz11.txt") as file:
    for line in file:
        line = line.strip()
        current = [0 if i == "." else 1 for i in line]
        # print(current)
        data.append(current)
        
    print("\n")

def createSpace(data):
    for i in range(len(data)-1,-1,-1):
        if data[i].count(1) == 0:
            data[i] = ["2-" for i in data[i]]

    data = list(map(list, zip(*data)))

    for i in range(len(data)-1,-1,-1):
        if data[i].count(1) == 0:
            data[i] = ["2|" if i != 2 else 4 for i in data[i]]

    data = list(map(list, zip(*data)))

    return(data)




def shortPath(pos1,pos2):
    total = 0
    prev = 0
    distance = 1000000   #expansion
    x= abs(pos1[0]-pos2[0])
    y= abs(pos1[1]-pos2[1])
    i = 0
    j = 0
    while pos1[0] + i != pos2[0] or pos1[1] + j != pos2[1]:    

        
        prevPosX, prevPosY = i,j
        if pos1[0] + i != pos2[0]:
            if pos1[0] + i < pos2[0]:
                i += 1
            else:
                i-= 1
        elif pos1[1] + j != pos2[1]:
            if pos1[1] + j < pos2[1]:
                j+= 1
            else:
                j-=1
        
        if type(data[pos1[0] + prevPosX][pos1[1] + prevPosY]) is str and type(data[pos1[0]+i][pos1[1]+j]) is str:
            if data[pos1[0]+i][pos1[1]+j][0] == "4"   or    (prevPosX != i and data[pos1[0]+i][pos1[1]+j][1] == "-") or (prevPosY != j and data[pos1[0]+i][pos1[1]+j][1] == "|"):
                total += distance
            else:
                total += 1
        elif type(data[pos1[0]+i][pos1[1]+j]) is str:
            if (prevPosX != i and data[pos1[0]+i][pos1[1]+j][1] == "-") or (prevPosY != j and data[pos1[0]+i][pos1[1]+j][1] == "|"):
                total += distance
            else:
                total += 1
        else: 
            total += 1

                
        prev = data[pos1[0]+i][pos1[1]+j]

    return(total)
        
            

def getAllGalaxies(data):
    allPos = []
    for i in range(len(data)-1,-1,-1):
        for j in range(len(data[i])):
            if data[i][j] == 1:
                allPos.append([i,j])
    return(allPos)


data = createSpace(data)

for i in data:
    print(i)
print("\n")
allGal =  getAllGalaxies(data)

def finalSum(allGal):
    allDist = []
    for i in range(len(allGal)-1,-1,-1):
        for j in range(len(allGal)):
            allDist.append(shortPath(allGal[i],allGal[j]))
        allGal.pop()
    return(sum(allDist))

finalSu = finalSum(allGal)
print(finalSu)