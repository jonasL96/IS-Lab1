import random
import array
import numpy

end = 1
executions = 0
#newfile for debug information
file_pointer = open("debug.txt","w+")

while end == 1:
    f = open('data.txt', 'r')
    file_pointer.write("Execution #%d\n" % (executions))
    #print("From beginning") #debug for unlimited executions
    #reading from a file
    for line in f:
        numbs = f.readlines()

    #Now to convert the list to a proper array that we can work with
    stri = ''.join(numbs) #converting to string to easily remove comma
    stri = stri.replace("\n",",") #changing newline to comma for next step
    stri = stri.split(",")
    numb_array = numpy.asarray(stri) #converting to numerical array
    numb_array = numb_array.astype(numpy.float32)#converting everything to float so it works
    w1 = random.uniform(-1,1)  #random in range of -1 to 1 (can be double)
    w2 = random.uniform(-1,1)
    b = random.uniform(-1,1)
    eta = 0.5 # starting eta value

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
    calculations = 0
    #perceptron training algorithm
    while e_total != 0:
        if q == len(x1): #each execution uses new x1 and x2 values, so after limit we reset to 0
            q = 0
        calculations = calculations + 1
        i = 0
        #initial parameter update for current example
        w1 = w1 + eta*e_total*x1[q]
        w2 = w2 + eta*e_total*x2[q]
        b = b + eta * e_total
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
        #to make every e value abs
        #while r < len(e):
            #e[r] = abs(e[r])
            #r = r + 1
            #if r == len(e):
                #r = 0
                #e_total = sum(e)
                #break
        e_total = sum(e)
        q = q + 1
        file_pointer.write("%d\n" % (e_total))
        #print(e_total)
        if calculations > 3000:
            print("Learning algorithm couldn't find correct answer in 1500 calculations. e_total last value was: ",e_total)
            file_pointer.close()
            break
    if calculations != 3001:
        print("It took", calculations ,"calculations of learning algorithm for no errors to be found.")
        executions = executions + 1
        file_pointer.write("Amount of calculations it took during this cycle %d\n" % (calculations))
    elif calculations > 3000:
        print("Amount of executions is equal to",executions)
        break
