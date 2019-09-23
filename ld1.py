import random
import array
import numpy
import math
import matplotlib.pyplot as plot

f = open('data.txt', 'r')

#reading from a file
for line in f:
    numbs = f.readlines()

#print(numbs)
#Now to convert the list to a proper array that we can work with
stri = ''.join(numbs) #converting to string to easily remove comma
stri = stri.replace("\n",",") #changing newline to comma for next step
stri = stri.split(",")
numb_array = numpy.asarray(stri) #converting to numerical array
numb_array = numb_array.astype(numpy.float32)#converting everything to float so it works
#print(numb_array) #debug
w1 = random.uniform(-1,1)  #random in range of 0 to 1 (can be double)
w2 = random.uniform(-1,1)
b = random.uniform(-1,1)
eta = 0.01 # starting eta value

i = 0

#splitting the array for perceptron
x1 = numb_array[::3]
x2 = numb_array[1::3]
d = numb_array[2::3]
e = [0.0] * 12

while i < len(x1):
    ans = w1*x1[i]+w2*x2[i]+b
    #print(ans) #debug
    ans = round(ans,2)
    if ans > 0:
        y = 1
    else:
        y = -1
    e[i] = d[i] - y
    i = i+1

e_total = 0
i = 0
q = 0
r = 0
#Calculating the total error
#while i < len(e):
	 #e_total = numpy.abs(e_total) + numpy.abs(e[i])
	 #i = i + 1
e_total = sum(e)
#print(e_total) #initial value of e_total
calculations = 0
#perceptron training algorithm
while e_total != 0:
    if q == len(x1): #each execution uses new x1 and x2 values, so after limit we reset to 0
        q = 0
    print(e_total)
    calculations = calculations + 1
    i = 0
    w1 = w1 + eta*e_total*x1[q]
    w2 = w2 + eta*e_total*x2[q]
    b = b + eta * e_total
    ans = w1*x1[q]+w2*x2[q]+b
    ans = round(ans,2) #calculating current output
    if ans > 0:
        y = 1
    else:
        y = -1
    e[i] = d[q] - y #current error
    #parameter update
    w1 = w1 + eta*e[i]*x1[q]
    w2 = w2 + eta*e[i]*x2[q]
    b = b + eta * e[i]
    #now we test the updated w1, w2 and b
    while i < len(x1):
        ans = w1*x1[i]+w2*x2[i]+b
        ans = round(ans,2)
        if ans > 0:
            y = 1
        else:
            y = -1
        e[i] = d[i] - y
        i = i + 1
    #print("This first") #debug
    #to make every e value abs
    #while q < len(e):
        #e[q] = abs(e[q])
        #q = q + 1
        #print("This second") #debug
        #if q == len(e):
            #q = 0
            #break
    e_total = sum(e)
    q = q + 1
    #print(e_total)
    if calculations > 1000:
        print("Learning algorithm couldn't find correct answer in 1000 calculations. e_total last value was: ",e_total)
        break
if calculations != 1001:
    print("It took", calculations ,"calculations of learning algorithm for no errors to be found.")