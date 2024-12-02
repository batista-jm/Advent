file = "db2.txt"
totalSafe = 0

def testSafe(file, totalSafe):
    with open(file, "r") as file:
        for line in file:
            count = 0
            value = -1
            poppedIndex = -1
            safe = True
            decreasing = False
            numbers = line.strip().split(' ')
            intNumbers = list(map(int, numbers))
            # for x in range(len(intNumbers)-1):
            size = len(intNumbers) - 1
            x = 0
            while x < size:
                if intNumbers[x] > intNumbers[x+1]:
                    print (abs(intNumbers[x] - intNumbers[x+1]))
                    if abs(intNumbers[x] - intNumbers[x+1]) > 3 or abs(intNumbers[x] - intNumbers[x+1]) < 1 or (decreasing == False and x > 0):
                        safe = False
                        if (count > 1):
                            break
                        elif count ==1 :
                            safe=True
                            intNumbers.insert(poppedIndex, value)
                            intNumbers.pop(poppedIndex +1)
                            count = count + 1
                            x = 0
                        else :
                            safe = True
                            count = count + 1
                            poppedIndex = x
                            value = intNumbers[x]
                            intNumbers.pop(x)
                            x = 0
                            size = size -1 
                    else:
                        decreasing = True
                        x = x + 1
                else:
                    if decreasing == True:
                        safe = False
                        if (count > 1):
                            break
                        elif count ==1 :
                            safe=True
                            intNumbers.insert(poppedIndex, value)
                            intNumbers.pop(poppedIndex +1)
                            count = count + 1
                            x = 0
                        else :
                            safe = True
                            count = count + 1
                            poppedIndex = x
                            value = intNumbers[x]
                            intNumbers.pop(x)
                            x = 0
                            size = size -1 
                    elif abs(intNumbers[x] - intNumbers[x+1]) > 3 or abs(intNumbers[x] - intNumbers[x+1]) < 1:
                        safe = False
                        
                        decreasing = False
                        if (count > 1):
                            break
                        elif count ==1 :
                            safe=True
                            intNumbers.insert(poppedIndex, value)
                            intNumbers.pop(poppedIndex +1)
                            count = count + 1
                            x = 0
                        else :
                            safe = True
                            count = count + 1
                            poppedIndex = x
                            value = intNumbers[x]
                            intNumbers.pop(x)
                            x = 0
                            size = size -1 
                        

                    
                    else:
                        
                        decreasing = False
                        x=x+1
                
                        
            if safe == True:
                totalSafe = totalSafe +1
            print(safe)

        print(totalSafe)


testSafe(file, totalSafe)