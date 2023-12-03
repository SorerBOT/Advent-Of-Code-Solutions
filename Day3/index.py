file = open("./input.txt", 'r')
lines = file.readlines()
linelen = len(lines[0])
sum = 0
# Constants
DEBUG_MODE = False 
NUM_DEBUG_LINES = 10
DEBUG_LINE = 0 # 20 
# Helpers
def slice_two_dimensional_array(array, x1, x2, y1, y2):
    arr = []
    for row in range(y1, y2 + 1):
        if (row == -1 or row >= len(array)):
            continue
        arr.append(array[row][x1:x2+1])
    return arr
def debug_block(block, flag, number):
    for row in block:
        print(row)
    print("Added: " + number + ' ' + str(flag))
    print("Current sum:" + str(sum))
    print("")
def real_is_digit(char):
    return (char >= '0' and char <= '9')
def is_symbol_character(character):
    return (character != '.' and character != '\n' and (not real_is_digit(character)))
def is_symbol(x, y):
    if (linelen-2 < x or len(lines)-1 < y):
        return False
    character = lines[y][x]
    return is_symbol_character(character)
def is_above_or_below(x,y): 
    return (is_symbol(x, y-1) or is_symbol(x, y+1)) 
def is_at_start_or_end(line, start, end): 
    return (is_symbol(start-1, line) or is_symbol(end+1, line))
def get_block_type(line): 
    if (line == 0):
        return "topless" 
    if (line == len(lines)-1):
        return "bottomless"
    return "regular"
def checkblock(block, blocktype, line=-1):
    newString = ""
    print(block)
    if (len(block[0]) == 0):
        return False
    if (blocktype == "regular"):
        newString = block[0] + block[2] + block[1][0] + block[1][-1]
    elif (blocktype == "topless"):
        newString = block[0][0] + block[0][-1] + block[1]
    elif (blocktype == "bottomless"):
        newString = block[0] + block[1][0] + block[1][-1]
    for character in newString:
        if (is_symbol_character(character)):
            if (line == DEBUG_LINE):
                print("Character: " + character)
            return True
    return False
for i in range(NUM_DEBUG_LINES if DEBUG_MODE else len(lines)):
    j = 0
    while (j <len(lines[i])-1):
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
        y2 = i if i == len(lines) else i+1
        block = slice_two_dimensional_array(lines, x1, x2, y1, y2)
        flag = checkblock(block, get_block_type(i), i)
        if (flag):
            sum += int(number)
        if (DEBUG_MODE and i == DEBUG_LINE):
            debug_block(block, flag, number)
        j = numEnd + 1
print("Sum: " + str(sum))
file.close()
