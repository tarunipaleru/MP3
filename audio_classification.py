import math
import sys

def freq(data):
    row=[]
    for i in range(25):   
        col=[]
        for j in range(10):
            zero_count = 0
            one_count = 0
            for image in range(len(data)):
                if data[image][i][j]== 0:
                    zero_count += 1
                elif data[image][i][j] == 1: 
                    one_count +=1
            col.append([zero_count, one_count])
        row.append(col)
    return row

def likelihood_calc(data, freq):
    #yes_train
    #freq_yes_train
    row=[]
    for i in range(25):   
        col=[]
        for j in range(10):
            pcount = 0
            freq_zero = freq[i][j][0]
            freq_one = freq[i][j][1]
            #for image in range(len(data)):
            #    if data[image][i][j]!= 0:
            #        pcount += 1
            #the 0.1 accounts for the smoothing that provides the highest accuracy
            col.append((freq_one+3.5)/float(len(data)+3.5*2))
        row.append(col)
    return row 

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

file_train = open('no_train.txt', 'r')
file_train_lines = file_train.readlines()

no_train = []
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
            no_train.append(image)
            image = []
        linecount += 1
        endcount += 1

#print yes_train
yes_freq = []
yes_freq = freq(yes_train)
no_freq = []
no_freq = freq(no_train)
#print "No Freq:\n"
#print no_freq
#print "\n"
#print "Yes Freq:\n"
#print yes_freq
#print "\n"

likelihood_yes_train = likelihood_calc(yes_train, yes_freq)  
#print likelihood_yes_train
likelihood_no_train = likelihood_calc(no_train, no_freq)  
#print likelihood_no_train
