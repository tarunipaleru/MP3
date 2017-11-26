import math
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
    for digit in range(10):
        count = freq[str(digit)]
        row=[]
        for i in range(28):   
            col=[]
            for j in range(28):
                pcount = 0
                for image in range(0,4999):
                    if data[image][i][j]!= 0 and int(label[image]) == digit:
                        pcount += 1
                #the 10 accounts for the smoothing
                col.append((pcount+10)/float(count+10*2))
            row.append(col)
        calculations.append(row)
    return calculations   

#trained values
train_freq = frequencies_prior(labels)
train_likelihoods = likelihood_calc(data, labels, train_freq)

# smoothing
# def smooth(likelihood, label, freq):
#     calc_smooth=[]
#     for digit in range(10):
#         count = freq[str(digit)]
#         row=[]
#         for i in range(28):   
#             col=[]
#             for j in range(28):
#                 pcount = 0
#                 if likelihood[digit][i][j]!= 0 and (label[digit]) == digit:
#                     pcount += 1
#                 col.append((pcount+1)/float(count+1*2))
#             row.append(col)
#         calc_smooth.append(row)
#     return calc_smooth   
                
# smooth_likelihood = smooth(train_likelihoods, labels, train_freq)

def MAP_calc():    
    TestList=[]
    x=0
    Prototypical= []
    for image in data_test:
        MAP=[]
        for digit in range(10):
            result=0
            result+=math.log(train_freq[str(digit)]/5000.0)
            for i in range(28):
                for j in range(28):
                    if image[i][j]!= 1:
                        result += math.log(1-train_likelihoods[digit][i][j])
                    else:
                        result += math.log(train_likelihoods[digit][i][j])  
            MAP.append(result)
        prediction= MAP.index(max(MAP))
        Prototypical.append((max(MAP),x))
        TestList.append(prediction)
        x = x+1
    return TestList, prediction, Prototypical

Test, Pred, Proto = MAP_calc()

def accuracy():
    count = 0
    for i in range(999):
        if Test[i] == (labels_test[i]):
            count = count + 1
    final = count/1000.0
    return final 

accuracy_score = accuracy()
print ('Accuracy Score: ' + str(accuracy_score))

def classification():
    classify=[]
    for digit in range(10):
        rate = 0.0
        classcount = 0
        for image in range(999):
            if digit == int(labels_test[image]):
                classcount+=1
                if digit == Test[image]:
                    rate+=1
        print('Classification for ' + str(digit)+ ' = ' + str(round(rate/classcount,6)*100))
        classify.append(rate)
classification()

def confusion():
    matrix=[]
    for x in range(10):
        col = []
        for y in range(10):
            classcount=0
            confusion=0
            for image in range(999):
                if Test[image] == y and int(labels_test[image])== x:
                    confusion+=1
                if x == int(labels_test[image]):
                    classcount+=1
            col.append(round(confusion/float(classcount), 4))
        matrix.append(col)
    return matrix

#Print confusion matrix
confusionMatrix = confusion()

def print_confusion(matrix):
    for row in matrix:
        string = ''
        for col in row:
            string += str(col)+' '
        print(string)

print_confusion(confusionMatrix)

def print_Posterior():
    digit_val=[]
    for digit in range(10):
        val=[]
        for image in range(999):
            if Test[image] == digit:
                if int(labels_test[image]) == digit:
                    val.append(Proto[image])
        
        low=min(val)
        print ('Lowest Posterior Probability for ' + str(digit))
        
        for row in data_test[low[1]]:
            string_low = ''
            for col in row:
                string_low += str(col)+''
            print(string_low)
        
        high=max(val)
        print ('Highest Posterior Probability for ' + str(digit))
        
        for row in data_test[high[1]]:
            string_high = ''
            for col in row:
                string_high += str(col)+''
            print(string_high)
        digit_val.append(val)

print_Posterior()



