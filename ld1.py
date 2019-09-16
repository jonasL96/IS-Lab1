import random
import array
import numpy
import math
import matplotlib.pyplot as plot

f = open('data.txt', 'r')

#reading from a file
for line in f:
    numbs = f.readlines()

print(numbs)
#Now to convert the list to a proper array that we can work with
stri = ''.join(numbs) #converting to string to easily remove comma
stri = stri.replace("\n",",") #changing newline to comma for next step
stri = stri.split(",")
numb_array = numpy.asarray(stri) #converting to numerical array
numb_array = numb_array.astype(numpy.float32)#converting everything to float so it works
#print(numb_array) #debug
w1 = random.uniform(-1,1)  #random in range of -1 to 1 (can be double)
w2 = random.uniform(-1,1)
b = random.uniform(-1,1)
eta = 0.1 # starting eta value

i = 0

#splitting the array for perceptron
x1 = numb_array[::3]
x2 = numb_array[1::3]
d = numb_array[2::3]
e = []

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
#Calculating the total error
while i < len(e)
	 e_total = abs(e_total) + abs(e[i])
	 i = i + 1

i = 0
#perceptron training algorithms
while e_total != 0:
    w1 = w1 + eta*e_total*x1[i]
    w2 = w2 + eta*e_total*x2[i]
    b = b + eta * e
    ans = w1*x1[i]+w2*x2[i]+b
    ans = round(ans,2)
    if ans > 0:
        y = 1
    else:
        y = -1
    e[i] = d[i] - y
    
    



	 