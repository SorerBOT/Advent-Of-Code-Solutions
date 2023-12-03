import re
file = open("./codes.txt", 'r')
sum = 0
for line in file:
    line = line.replace("one", 'one1one')
    line = line.replace("two", 'two2two')
    line = line.replace("three", 'three3three')
    line = line.replace("four", 'four4four')
    line = line.replace("five", 'five5five')
    line = line.replace("six", 'six6six')
    line = line.replace("seven", 'seven7seven')
    line = line.replace("eight", 'eight8eight')
    line = line.replace("nine", 'nine9nine')
    line = re.sub("\D", '', line)
    if len(line) > 0: 
        sum += int(line[0] + line[-1])
print(sum)
file.close()
