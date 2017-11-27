import math
import sys

file_train = open('yes_train.txt', 'r')
file_train_lines = file_train.readlines()

yes_train = []
image = []
linecount = 0
endcount = 0
for line in file_train_lines:
    if linecount == 30:
        yes_train.append(image)
        image = []
        linecount = 0
        endcount += 3
    if endcount == 3920:
        break
    line_val = []
    for char in line:
        if char == '%':
            line_val.append(1)
        else:
            line_val.append(0)
    linecount += 1
    endcount += 1
    image.append(line_val)

#print yes_train
freq_yes_train = len(yes_train)

file_train_no = open('no_train.txt', 'r')
file_train_lines_no = file_train_no.readlines()

no_train = []
image_no = []
linecount1 = 0
endcount1 = 0
for line in file_train_lines_no:
    if linecount1 == 30:
        no_train.append(image_no)
        image_no = []
        linecount1 = 0
        endcount1 += 3
    if endcount1 == 3920:
        break
    line_val = []
    for char in line:
        if char == '%':
            line_val.append(1)
        else:
            line_val.append(0)
    linecount1 += 1
    endcount1 += 1
    image_no.append(line_val)

# print no_train
freq_no_train = len(no_train)
# print(freq_no_train)

file_test= open('yes_test.txt', 'r')
file_test_lines = file_test.readlines()

yes_test = []
image_y_test = []
linecount2 = 0
endcount2 = 0
for line in file_test_lines:
    if linecount2 == 30:
        yes_test.append(image_y_test)
        image_y_test = []
        linecount2 = 0
        endcount2 += 3
    if endcount2 == 3920:
        break
    line_val = []
    for char in line:
        if char == '%':
            line_val.append(1)
        else:
            line_val.append(0)
    linecount2 += 1
    endcount2 += 1
    image_y_test.append(line_val)

#print yes_test
freq_yes_test = len(yes_test)
#print(freq_yes_test)

file_test_n = open('no_test.txt', 'r')
file_test_lines_n = file_test_n.readlines()

no_test = []
image_n_test = []
linecount3 = 0
endcount3 = 0
for line in file_test_lines_n:
    if linecount3 == 30:
        no_test.append(image_n_test)
        image_n_test = []
        linecount3 = 0
        endcount3 += 3
    if endcount3 == 3920:
        break
    line_val = []
    for char in line:
        if char == '%':
            line_val.append(1)
        else:
            line_val.append(0)
    linecount3 += 1
    endcount3 += 1
    image_n_test.append(line_val)

print no_test
freq_no_test = len(no_test)
print(freq_no_test)


