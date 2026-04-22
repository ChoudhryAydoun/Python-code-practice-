#LINEAR SEARCH
  
#Declare arrayData : ARRAY[0:9] OF Integer
arrayData = [10 , 5 ,6 , 7 ,1 ,12 , 13 , 15 , 21, 8]
##Q2
def linearsearch(number):
    for x in range(10):
        if number == arrayData[x]:
            return True
    return False
num = linearsearch(7)
print (num)

#Q3
num2 = int(input("Enter the num :"))
found = linearsearch(num2)
if found == True :
    print("It is found")
else:
    print("Not found")
##############################################
# BINARY SEARCH
  
#Q Write the Binary Search Function and take the integer to be found as Parameter and return True if 
#found and false if not found.
#Declare arraydata : ARRAY[0 : 9] OF Integer
#Declare lowerbound , upperbound : Integer
arraydata = [1 , 5  ,6 , 7 , 8 , 10,  12 , 13 , 15 ,21 ]
def binarysearch(number):
    lowerbound = 0 
    upperbound = 9#or also write(len(arraydata))-1 it will give 10 -1 = 9
    while lowerbound <= upperbound:
        midpoint = int((lowerbound + upperbound) / 2)
        
        if arraydata[midpoint] == number:
            return True#you can put midpoint if they ask to print the index instead of true or false.
        
        elif number < arraydata[midpoint]:
            upperbound = midpoint - 1 

        else:
            lowerbound = midpoint + 1

    return False

temp = binarysearch(5)
print(temp)
if temp == True:
    print("Value Found")
else:
    print("Value Not Found")
    
    
"""binarysearch(5)
   print(arraydata)
   cannnot happen because it is not already sorted we are not sorting we are searching."""