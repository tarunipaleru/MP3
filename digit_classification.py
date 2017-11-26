from math import log
import sys

#cleaning data to get all the test and training data and labels
file_train = open('trainingimages', 'r')
file_train_lines = file_train.readlines()

data = []
image = []
linecount = 0
for line in file_train_lines:
    if linecount == 28:
        data.append(image)
        image = []
        linecount = 0
    line_val = []
    for char in line:
        if char == ' ':
            line_val.append(0)
        else:
            line_val.append(1)
    linecount += 1
    image.append(line_val)

file_label = open('traininglabels', 'r')
file_label_lines = file_label.readlines()

labels = []
for label in file_label_lines:
    label = label.strip('\n')
    labels.append(str(label))

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

data_test = []
image_test = []
linecount_test = 0
for line in file_test_lines:
    if linecount_test == 28:
        data_test.append(image_test)
        image_test = []
        linecount_test = 0
    line_val = []
    for char in line:
        if char == ' ':
            line_val.append(0)
        else:
            line_val.append(1)
    linecount_test += 1
    image_test.append(line_val)

file_label_test = open('testlabels', 'r')
file_label_test_lines = file_label_test.readlines()

labels_test = []
for label in file_label_test_lines:
    label = label.strip('\n')
    labels_test.append(int(label))

#calculating frequences
def frequencies_prior(labels):
    freq = {}
    for i in labels:
        if i in freq.keys():
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

#estimating likelihoods 
def likelihood_calc(data, label, freq):
    calculations=[]
    for digit in range(0, 10):
        examplecount = freq[str(digit)]
        row=[]
        for i in range(0, 28):   
            col=[]
            for j in range(0, 28):
                pcount = 0
                for image in range(0,4999):
                    if data[image][i][j]!= 0 and int(label[image])== digit:
                        pcount += 1
                col.append(round((pcount+1)/float(examplecount+1*2),3))
            row.append(col)
        calculations.append(row)
    return calculations   

def train_model():
    train_freq = frequencies_prior(labels):
    train_likelihoods = likelihood_calc(data, labels, train_freq)
    return train_freq, train_likelihoods





