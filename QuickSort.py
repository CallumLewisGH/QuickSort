#QuikSort
inputList = [5,1,3,7,11,3,9,6]

def quickSort(inputList):
    if len(inputList) > 1:
        pivot = inputList[-1]
        inputList = inputList[0:-1]
        lowerList = []
        upperList = []

        for i in inputList:
            if i > pivot:
                upperList.append(i)

            else:
                lowerList.append(i)
    
        return quickSort(lowerList) + [pivot] + quickSort(upperList)
    else:
        return inputList
    
print(quickSort(inputList))
    
    






