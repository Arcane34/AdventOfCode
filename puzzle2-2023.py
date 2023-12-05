example = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

# Solution Part 1

total = 0
games = []
stats = []
with open('puz2.txt') as fp:
    for line in fp:
        games.append(line.split(":")[0])
        stat = line.split(":")[1].strip()
        picks = stat.split(";")
        values = [i.split(",") for i in picks]
        colours = []
        for i in values:
            colour = [0,0,0]
            for col in i:
                current = col.split(" ")
                if current[0] == '':
                    current = current[1:]


                if current[1] == "red":
                    colour[0] = int(current[0])
                elif current[1] == "green":
                    colour[1] = int(current[0])
                elif current[1] == "blue":
                    colour[2] = int(current[0])

            colours.append(colour)
        stats.append(colours)

    
indexes = []
# invalid games
for i in range(len(stats)):
    if len([j[0] for j in stats[i] if j[0] > 12]) != 0:
        indexes.append(i+1)
    elif len([j[1] for j in stats[i] if j[1] > 13]) != 0:
        indexes.append(i+1)
    elif len([j[2] for j in stats[i] if j[2] > 14]) != 0:
        indexes.append(i+1)




# valid games aka complement of indexes
x = [i+1 for i in range(len(stats))]
for i in indexes:
    x.remove(i)

print(sum(x))


#Solution Part 2
total = 0
for i in range(len(stats)):
    mini = max([j[0] for j in stats[i]]) * max([j[1] for j in stats[i]]) * max([j[2] for j in stats[i]])
    total += mini

print(total)


# total = 0
# games = []
# stats = []
# for line in example.split("\n"):
#         games.append(line.split(":")[0])
#         stat = line.split(":")[1].strip()
#         picks = stat.split(";")
#         values = [i.split(",") for i in picks]
#         colours = []
#         for i in values:
#             colour = [0,0,0]
#             for col in i:
#                 current = col.split(" ")
#                 if current[0] == '':
#                     current = current[1:]


#                 if current[1] == "red":
#                     colour[0] = int(current[0])
#                 elif current[1] == "green":
#                     colour[1] = int(current[0])
#                 elif current[1] == "blue":
#                     colour[2] = int(current[0])

#             colours.append(colour)
#         stats.append(colours)

    
# indexes = []
# # invalid games
# for i in range(len(stats)):
#     if len([j[0] for j in stats[i] if j[0] > 12]) != 0:
#         indexes.append(i+1)
#     elif len([j[1] for j in stats[i] if j[1] > 13]) != 0:
#         indexes.append(i+1)
#     elif len([j[2] for j in stats[i] if j[2] > 14]) != 0:
#         indexes.append(i+1)




# # valid games aka complement of indexes
# x = [i+1 for i in range(len(stats))]
# for i in indexes:
#     x.remove(i)

# print(sum(x))

  