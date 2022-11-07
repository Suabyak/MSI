file = open("Expert Method/tags.csv", "r").read()

file = file.split("\n")
content = list()
for line in file:
    content.append(line.split(";")[:2])

possibilities = list()
for i in range(2**len(content)):
    tags = str(bin(i))[2:]
    tags = (6-len(tags)) * "0" + tags

    possibilities.append(tags)

result = ""
for tag in possibilities:
    result += "<nazwa>;"
    for i in range(len(tag)):
        result += content[i][int(tag[i])] + ";"
    result = result[:-1]
    result += "\n"
to_save = open("Expert Method/games.csv", "w")
to_save.write(result)
to_save.close()