inFile = open("task1.txt", "r")
outFile = open("task1outP.txt", "w")


line = inFile.readline()

total = 0

while line != "":
   
    value = float(line.lstrip("Hello"))
    outFile.write("%.2f\n"% (value))
    total += value

    print(total)
    line = inFile.readline()

outFile.write("---------------\n" )
outFile.write("Total : %.2f\n" % (total))

outFile.write("Average : %.2f\n" % (total / 5 ))

    
    

# print("##########"+line);