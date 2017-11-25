from math import log
import sys

file_train = open('trainingimages', 'r')
file_train_lines = file_train.readlines()

data = []
for line in file_train_lines:
    line = line.strip('\n')
    line_val = []
    for char in line:
        if char == ' ':
            line_val.append(0)
        else:
            line_val.append(1)
    data.append(line_val)
print data

file_label = open('traininglabels', 'r')
file_label_lines = file_label.readlines()

labels = []
for label in file_label_lines:
    label = label.strip('\n')
    labels.append(int(label))
