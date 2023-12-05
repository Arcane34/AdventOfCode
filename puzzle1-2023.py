# SOLUTION PART 1
# total = 0

# with open('puz1.txt') as fp:

#     for line in fp:

#         lineNums = []

#         for index in range(len(line)):

  

#             if line[index].isnumeric():

#                 lineNums.append(line[index])

#         print(lineNums)

#         total += int(lineNums[0] + lineNums[-1])

  
  

# print(total)


# SOLUTION PART 2"

numberNames = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero", "ten", "eleven", "twelve", "thirteen", "fifteen", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninty", "hundred"]
numberVals = [1,2,3,4,5,6,7,8,9,0,0,1,2,3,5,0,0,0,0,0,0,0,0,0]


total = 0
with open('puz1.txt') as fp:

    for line in fp:
            
        num = ""
        first = ""
        last = ""
        for index in range(len(line)):



            if not(line[index].isnumeric()):
                num += line[index]
                if index == len(line)-1:
                    if len(num) > 2:
                        indexes = []
                        for i in range(len(numberNames)-1, -1, -1):
                            temp = num
                            counter = 0
                            while numberNames[i] in num:
                                if numberNames[i] in [i[0] for i in indexes]:
                                    num = num.replace(numberNames[i],"",1)
                                    counter += 1
                                
                                if numberNames[i] in num:
                                    indexes.append([numberNames[i], num.index(numberNames[i])+ counter*len(numberNames[i])])
                            num = temp
                                
                        
                        if len(indexes) > 0:
                            first = indexes[[i[1] for i in indexes].index(min([i[1] for i in indexes]))][0]
                            indexes = []
                            break

            else:
                if num != "":
                    if len(num) > 2:
                        indexes = []
                        for i in range(len(numberNames)-1, -1, -1):
                            temp = num
                            counter = 0
                            while numberNames[i] in num:
                                if numberNames[i] in [i[0] for i in indexes]:
                                    num = num.replace(numberNames[i],"",1)
                                    counter += 1
                                
                                if numberNames[i] in num:
                                    indexes.append([numberNames[i], num.index(numberNames[i])+ counter*len(numberNames[i])])
                            num = temp
                                

                        if len(indexes) > 0:
                            first = indexes[[i[1] for i in indexes].index(min([i[1] for i in indexes]))][0]
                            indexes = []
                            break
                    num = ""
            

            if line[index].isnumeric():
                first = (line[index])
                break

        


        num = ""
        for index in range(len(line)-1,-1,-1):

            if not(line[index].isnumeric()):
                num = line[index] + num
                if index == 0:
                    if len(num) > 2:
                        indexes = []
                        for i in range(len(numberNames)-1, -1, -1):
                            
                            temp = num
                            counter = 0
                            while numberNames[i] in num:
                                if numberNames[i] in [i[0] for i in indexes]:
                                    num = num.replace(numberNames[i],"",1)
                                    counter += 1
                                
                                if numberNames[i] in num:
                                    indexes.append([numberNames[i], num.index(numberNames[i])+ counter*len(numberNames[i])])
                            num = temp
                                
                            
                        if len(indexes) > 0:
                            print(indexes)
                            last = indexes[[i[1] for i in indexes].index(max([i[1] for i in indexes]))][0]
                            indexes = []
                            break
            else:
                if num != "":
                    if len(num) > 2:
                        indexes = []
                        for i in range(len(numberNames)-1, -1, -1):
                        
                            temp = num
                            counter = 0
                            while numberNames[i] in num:
                                if numberNames[i] in [i[0] for i in indexes]:
                                    num = num.replace(numberNames[i],"",1)
                                    counter += 1
                                
                                if numberNames[i] in num:
                                    indexes.append([numberNames[i], num.index(numberNames[i])+ counter*len(numberNames[i])])
                            num = temp
                                

                        if len(indexes) > 0:
                        
                            print(indexes)
                            last = indexes[[i[1] for i in indexes].index(max([i[1] for i in indexes]))][0]
                            indexes = []
                            break
                    num = ""
            

            if line[index].isnumeric():
                last = (line[index])
                break



        

        if len(first) > 1:
            first = str(numberVals[numberNames.index(first)])
        

        if len(last) > 1:
            last = str(numberVals[numberNames.index(last)])

        print(first)
        print(last)
        print(line)
        print("\n")

        total += int(first + last)





print(total)
