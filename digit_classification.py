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

file_label = open('traininglabels', 'r')
file_label_lines = file_label.readlines()

labels = []
for label in file_label_lines:
    label = label.strip('\n')
    labels.append(int(label))

file_test = open('testimages', 'r')
file_test_lines = file_test.readlines()

data_test = []
for line in file_test_lines:
    line = line.strip('\n')
    line_val = []
    for char in line:
        if char == ' ':
            line_val.append(0)
        else:
            line_val.append(1)
    data_test.append(line_val)


file_label_test = open('testlabels', 'r')
file_label_test_lines = file_label_test.readlines()

labels_test = []
for label in file_label_test_lines:
    label = label.strip('\n')
    labels_test.append(int(label))



