global data
data = []
import datetime
import copy


with open("puz14.txt") as file:
    for line in file:
        line = line.strip()
        current = [i for i in line]
        data.append(current)

def printF(data):
    for i in data:
        print(''.join(i))
    print("\n")

printF(data)

def findR():
    rocks = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "O":
                rocks.append([i,j])
    return rocks


def rotate():
    temp = list(zip(*data[::-1]))
    n = []
    for i in temp:
        n.append(list(i))
    for i in range(len(data)):
        data[i] = n[i]

def roll():
    for rock in findR():
        tempXY = rock.copy()
        rolled = False
        change = False

        while not(rolled):
            if tempXY[0] != 0:
                if data[tempXY[0]-1][tempXY[1]] == ".":
                    tempXY = [tempXY[0]-1,tempXY[1]]
                    change = True
                else:
                    rolled = True
            else:
                rolled = True
        
        if change:
            data[rock[0]][rock[1]] = "."
            data[tempXY[0]][tempXY[1]] = "O"


def cycle():
    roll()  #n
    rotate()
    roll()  #w
    rotate()
    roll()  #s
    rotate()
    roll()  #e
    rotate()

def addEm(dat):
    total = 0
    for i in dat:
        total+=i.count("O")*(len(dat)-dat.index(i))
    return(total)
        
myList = [copy.deepcopy(data)]
ind = -1
it = 0
for i in range(1000000000):
    cycle()
    

    if data in myList:
        print("found it " + str(myList.index(data)))
        
        ind = myList.index(data)
        loop = myList[ind:]
        cyclen = len(loop)
        it = 1000000000- (i +1)
        newIndex = ((it) % len(loop)) 
        print(newIndex)
        print(addEm(loop[newIndex]))
        printF(myList[ind])
        break
    myList.append(copy.deepcopy(data))


