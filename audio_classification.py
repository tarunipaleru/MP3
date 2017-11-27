import math
import sys

file_train = open('yes_train.txt', 'r')
file_train_lines = file_train.readlines()

yes_train = []
image = []
linecount = 1
endcount = 1

for line in file_train_lines:
    if (linecount > 25):
        if (linecount == 28):
            linecount = 1
        else:
            linecount += 1
        endcount += 1
    elif endcount == 3920: 
        break
    else:
        line_val = []
        for char in line:
            if char == ' ':
                line_val.append(0)
            elif char == '%':
                line_val.append(1)
        image.append(line_val)
        if linecount == 25:
            yes_train.append(image)
            image = []
        linecount += 1
        endcount += 1

print yes_train