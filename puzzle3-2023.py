# SOLUTION PART 1


# symbols = []
# numbers = []
# with open('puz3.txt') as fp:
#     counter = 1
#     for line in fp:
    
#         num = ""
#         for character in range(len(line)):
#             if not(line[character].isnumeric()):
#                 if line[character] != "." and line[character] != '\n':
#                     symbols.append([counter, character, line[character]])
#                 if num != "" :
#                     numbers.append([int(num), counter ,[character-(len(num)-i) for i in range(len(num))]])
#                     num = ""
                

#             else:
#                 num += line[character]
                

#             if character == len(line)-1 and num != "":
#                 numbers.append([int(num), counter , [character-(len(num)-i) for i in range(len(num))]])
#                 num = ""

#         counter += 1

# ple = []
# total = 0
# for i in numbers:
#     for j in symbols:
        
#         if (j[0] -1 <= i[1] <= j[0] +1) and (j[1]-1 in i[2] or j[1] in i[2] or j[1]+1 in i[2]):
#             ple.append(i[0])
#             if i[0] == 158:
#                 print(i)
#             total += i[0]
#             break


# print(sum(ple))
# print(total)




# lines = []
# for i in range(140):
#     lines.append("............................................................................................................................................\n")

# for i in numbers:
#     # if i in ple:
#     #     for k in i[2]:
#     #         lines[i[1]-1] = lines[i[1]-1][:k] + "." + lines[i[1]-1][k+1:] 
#     # else:
#         counter = 0
#         for k in i[2]:
#             lines[i[1]-1] = lines[i[1]-1][:k] + str(i[0])[counter] + lines[i[1]-1][k+1:] 
#             counter += 1

# for i in symbols:
#     lines[i[0]-1] = lines[i[0]-1][:i[1]] + i[2] + lines[i[0]-1][i[1]+1:]  




# text = ""

# for i in lines:
#     text += i

# f = open("puz3A.txt", "w")
# f.write(text)
# f.close()






# SOLUTION PART 2

symbols = []
numbers = []
with open('puz3.txt') as fp:
    counter = 1
    for line in fp:
    
        num = ""
        for character in range(len(line)):
            if not(line[character].isnumeric()):
                if line[character] != "." and line[character] != '\n':
                    symbols.append([counter, character, line[character]])
                if num != "" :
                    numbers.append([int(num), counter ,[character-(len(num)-i) for i in range(len(num))]])
                    num = ""
                

            else:
                num += line[character]
                

            if character == len(line)-1 and num != "":
                numbers.append([int(num), counter , [character-(len(num)-i) for i in range(len(num))]])
                num = ""

        counter += 1


ple = []
total = 0
for i in numbers:
    for j in symbols:
        
        if (j[0] -1 <= i[1] <= j[0] +1) and (j[1]-1 in i[2] or j[1] in i[2] or j[1]+1 in i[2]):
            ple.append([j,i])
            total += i[0]
            break


newSymbols = [i[0] for i in ple if i[0][2] == "*"]
noice = []
for i in newSymbols:
    if newSymbols.count(i) == 2:
        noice.append(i)

for i in range(len(noice)-1, -1,-1):
    if noice.count(noice[i]) == 2:
        noice.remove(noice[i])
noice.sort()
print(noice)

total = 0
for i in noice:
    partss = [j[1][0] for j in ple if j[0] == i]
    print(partss[0]*partss[1])
    total += partss[0]*partss[1]

print(total)
