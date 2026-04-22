#def Average(sum , count):
  #  print (sum / count)

#Average (6 ,2)


# Question number 2 

def table(i):
    for x in range (1 , 11):
         tab = i * x
         print( str(i) + ' X' +" " + str(x)  + "= " + str(tab) )

#table(2) # you dont have to write print it give a line gap in the answer only write table(number in bracket or user input)
#and if array so only do array() leave bracket empty nothing inside it 

#Q3 Create a function for finding the largest value in an array and then print the table of that number 

Number = [45 , 34 , 23 ,87 , 96 , 23  ]
def largest (arraytemp):
     largenum = arraytemp[0]
     for x in range (1 , len(arraytemp)): 
       if arraytemp[x] > largenum:
          largenum = arraytemp[x]
     return largenum 

largestnumberarray = largest(Number)
table(largestnumberarray)
print(table)         
