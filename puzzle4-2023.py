

# SOLUTION PART 1

# total = 0
# with open('puz4.txt') as fp:
#     counter = 1
#     for line in fp:
#         l = line.split(":")
#         iD = l[0]
#         splitNums = l[1].split("|")
#         winNums = [int(i) for i in splitNums[0].strip().split(" ") if i != '']
#         nums = [int(i) for i in splitNums[1].strip().split(" ") if i != '']
#         winNums.sort()
#         nums.sort()
#         numberOfWin = len([i for i in winNums if i in nums])
#         numOfWins.append(numberOfWin)
        
#         if numberOfWin > 0:
#             total += 2**(numberOfWin-1)
        
# print(total)

# SOLUTION PART 2

numOfWins = []
total = 0
with open('puz4.txt') as fp:
    counter = 1
    for line in fp:
        l = line.split(":")
        iD = l[0]
        splitNums = l[1].split("|")
        winNums = [int(i) for i in splitNums[0].strip().split(" ") if i != '']
        nums = [int(i) for i in splitNums[1].strip().split(" ") if i != '']
        winNums.sort()
        nums.sort()
        numberOfWin = len([i for i in winNums if i in nums])
        numOfWins.append([counter, numberOfWin])
        
        
        counter += 1
        

def scratchCardsWon(num):
    cards = 1
    for i in range(numOfWins[num-1][1]):
        cards += scratchCardsWon(num+1+i)
    return cards
    
for i in range(len(numOfWins)):
    total += scratchCardsWon(i+1)

print(total)
