import re

file = open('./input.txt', 'r')
sum = 0
for line in file.readlines():
    gameround = re.findall("( ?\d+ \w+,?+;?)", line)
    gamedict = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for roll in gameround:
        rollresult = re.search("(\d+) (\w+)", roll)
        number = int(rollresult.group(1))
        color = rollresult.group(2)
        if (gamedict[color] < number):
            gamedict[color] = number
    sum += gamedict["red"] * gamedict["green"] * gamedict["blue"]
print(sum)
file.close()
