#Sum of list recursively
def listsum(numList):
    #Used to not waste the time of the function if their is only one element in the list inputted
   if len(numList) == 1:
        return numList[0]
   else:
       #add the first element to everything after the second element including the second element
       sumOfList = numList[0] + listsum(numList[1:]
    #Used to output the sum of the list
       return sumOfList

print(listsum([1,3,5,7,9]))

