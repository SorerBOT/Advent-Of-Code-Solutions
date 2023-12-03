import re

file = open('./input.txt', 'r')
sum = 0
for line in file.readlines():
    gamevalid = True
    gameidres = re.search("Game (\d+): (( ?\d+)( \w+,?)+;?)+", line)
    gameid = int(gameidres.group(1))
    gameround = re.findall("( ?\d+ \w+,?+;?)", line)
    for roll in gameround:
        gamedict = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        rollresult = re.search("(\d+) (\w+)", roll)
        number = rollresult.group(1)
        color = rollresult.group(2)
        gamedict[color] += int(number)
        if (gamedict["red"] > 12 or gamedict["green"] > 13 or gamedict["blue"] > 14):
            gamevalid = False
    if (gamevalid):
        sum += gameid
print(sum)
file.close()
