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
w1 = random.uniform(0,1)  #random in range of -1 to 1 (can be double)
w2 = random.uniform(0,1)
b = random.uniform(0,1)
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
#Calculating the total error
while i < len(e):
	 e_total = numpy.abs(e_total) + numpy.abs(e[i])
	 i = i + 1

calculations = 0
#perceptron training algorithm
while e_total != 0:
    calculations = calculations + 1
    i = 0
    w1 = w1 + eta*e_total*x1[i]
    w2 = w2 + eta*e_total*x2[i]
    b = b + eta * e[i]
    ans = w1*x1[i]+w2*x2[i]+b
    ans = round(ans,2)
    if ans > 0:
        y = 1
    else:
        y = -1
    e[i] = d[i] - y
    w1 = w1 + eta*e[i]*x1[i]
    w2 = w2 + eta*e[i]*x2[i]
    b = b + eta * e[i]
    while i < len(x1):
        ans = w1*x1[i]+w2*x2[i]+b
        ans = round(ans,2)
        if ans > 0:
            y = 1
        else:
            y = -1
        e[i] = d[i] - y
        i = i + 1
    #to make every e value abs
    while q < len(e):
        e[q] = abs(e[q])
       # print(e[q])
        q = q + 1
        if q == len(e):
            q = 0
            break
    e_total = sum(e)
    print(e_total)

print("It took only ", calculations ," calculations of learning algorithm for no errors to be found.")