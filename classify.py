import math
import sys

file_train = open('yes_train.txt', 'r')
file_train_lines = file_train.readlines()

yes = []
image = []
linecount = 0
for line in file_train_lines:
    if linecount == 30:
        yes.append(image)
        image = []
        linecount = 0
    line_val = []
    for char in line:
        if char == '%':
            line_val.append(1)
        elif char == ' ':
            line_val.append(0)
    linecount += 1
    image.append(line_val)

freq_yes = len(yes)

file_test_y = open('yes_test.txt', 'r')
file_test_y_lines = file_test_y.readlines()

yes_test = []
image_test = []
linecount1 = 0
for line in file_test_y_lines:
    if linecount1 == 30:
        yes_test.append(image_test)
        image_test = []
        linecount1 = 0
    line_val = []
    for char in line:
        if char == '%':
            line_val.append(1)
        elif char == ' ':
            line_val.append(0)
    linecount1 += 1
    image_test.append(line_val)

freq_yes_test = len(yes_test)

file_train_n = open('no_train.txt', 'r')
file_train_lines_n = file_train_n.readlines()

no_train = []
image_train_n = []
linecount2 = 0
for line in file_train_lines_n:
    if linecount2 == 30:
        no_train.append(image_train_n)
        image_train_n = []
        linecount2 = 0
    line_val = []
    for char in line:
        if char == '%':
            line_val.append(1)
        elif char == ' ':
            line_val.append(0)
    linecount2 += 1
    image_train_n.append(line_val)

freq_no = len(no_train)

file_test_n = open('no_test.txt', 'r')
file_test_n_lines = file_test_y.readlines()

no_test = []
image_test_n = []
linecount3 = 0
for line in file_test_y_lines:
    if linecount3 == 30:
        no_test.append(image_test_n)
        image_test_n = []
        linecount3 = 0
    line_val = []
    for char in line:
        if char == '%':
            line_val.append(1)
        elif char == ' ':
            line_val.append(0)
    linecount3 += 1
    image_test_n.append(line_val)
print no_test
freq_no_test = len(no_test)
print freq_no_test




