def real_is_digit(char):
    return (char >= '0' and char <= '9')

file = open("./input.txt", 'r')
lines = file.readlines()
linelen = len(lines[0])
sum = 0
gear_list = []
for i in range(len(lines)):
    j = 0
    while (j < len(lines[i])-1):
        if (not real_is_digit(lines[i][j])):
            j += 1
            continue
        number = lines[i][j]
        numEnd = j + 1
        while (real_is_digit(lines[i][numEnd])):
            number += lines[i][numEnd]
            numEnd += 1
        numEnd -= 1
        x1 = 0 if j == 0 else j-1
        x2 = numEnd if numEnd == linelen else numEnd+1
        y1 = i if i == 0 else i-1
        y2 = i if i == len(lines) - 1 else i + 1
        for x in range(x1, x2 + 1):
            if (lines[y1][x] == '*'):
                gear_list.append({
                    "gear": {
                        "x": x,
                        "y": y1
                    },
                    "number": int(number)
                })
            if (lines[y2][x] == '*'):
                gear_list.append({
                    "gear": {
                        "x": x,
                        "y": y2
                    },
                    "number": int(number)
                })
        for y in range(y1 + 1, y2):
            if (lines[y][x1] == '*'):
                gear_list.append({
                    "gear": {
                        "x": x1,
                        "y": y
                    },
                    "number": int(number)
                })
            if (lines[y][x2] == '*'):
                gear_list.append({
                    "gear": {
                        "x": x2,
                        "y": y
                    },
                    "number": int(number)
                })
        j = numEnd + 1
for i in range(len(lines)):
    j = 0
    while (j < len(lines[i])-1):
        filtered = list(filter(lambda gear: gear["gear"]["x"] == j and gear["gear"]["y"] == i, gear_list))
        j += 1
        if (len(filtered) != 2):
            continue
        sum += filtered[0]["number"] * filtered[1]["number"]
print("Sum: " + str(sum))
file.close()
