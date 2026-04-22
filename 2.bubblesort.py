# Efficient code
arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]
def bubblesort():
    Noswaps = False
    Boundary = 9  #one less then len of arraydata.
    while Noswaps == False:
        Noswaps = True 
        for y in range (Boundary ):
            if arrayData[y] > arrayData[y + 1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y + 1]
                arrayData[y + 1] = temp
                Noswaps = False
        Boundary = Boundary - 1
bubblesort()
print(arrayData)#always run a function and then print array it is only for array.

#Q Create an array of words. Sort them alphabetically using the bubble sort technique? Question form word 



