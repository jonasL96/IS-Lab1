import random
import array
import numpy
import math
import pandas
import matplotlib.pyplot as plot

#Results to classes
class results_one:
    def __init__(self):
        self.results = []

    def insertResult_one(self,result, index):
        self.results.insert(index,result)
       # print(self.results) #debug

    def print_result(self):
        print(self.results)


class results_two:
    def __init__(self):
        self.results = []

    def insertResult_two(self, result, index):
        self.results.insert(index,result)
       # print(self.results) #debug

    def print_result(self):
        print(self.results)


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
eta = 0.01 # starting eta value

i = 0
q = 0
indx1 = 0
indx2 = 0

ans1 = results_one()
ans2 = results_two()

#splitting the array for perceptron
#print(numb_array) #pre split
x1 = numb_array[::3]
x2 = numb_array[1::3]
d = numb_array[2::3]
#print(x1)#debug
#print(x2)#debug
#print(d)#debug

while i < len(x1):
    ans = w1*x1[i]+w2*x2[i]+b
    #print(ans) #debug
    q = q + 1
    ans = round(ans,2)
    if ans > 0:
        y = 1
        ans1.insertResult_one(q,indx1) #which elements from data.txt was it
        indx1 = indx1 + 1
        ans1.insertResult_one(ans,indx1) #which elements from data.txt was it
        indx1 = indx1 + 1
    elif ans <= 0:
        y = -1
        ans2.insertResult_two(q,indx2) #which elements from data.txt was it
        indx2 = indx2 + 1
        ans2.insertResult_two(ans,indx2) #which elements from data.txt was it
        indx2 = indx2 + 1
    e = d[i] - y
    w1 = w1 + eta*e*x1[i]
    w2 = w2 + eta*e*x2[i]
    b = b + eta * e
    i = i+1

#Results in groups:
ans1.print_result()
ans2.print_result()