# sometimes the examiner say you to write the klinked list in 2D array instead of record datatype Node which we 
#make through the help of class and constructor

startpointer = 0 
linkedlist = [[1, 1], [5 , 4], [6, 7], [7 , -1] , [2 ,2], [0 , 6],[0 , 8],[56 , 3],[0 , 9],[0 , -1]] 
emptylist = 5
def addnode():
    global startpointer
    global linkedlist
    global emptylist
    currentpointer = startpointer
    data = int(input("ENter the number"))
    if emptylist < 0 :
        return False 
    else:
        freelist = emptylist 
        emptylist = linkedlist[emptylist][1]

        newnode = [data , -1 ] #isko aisay likha tah mainay 2Darray mai [data][-1]
        linkedlist[freelist] = newnode

        previouspointer = 0
        while currentpointer != -1:
            previouspointer = currentpointer
            currentpointer = linkedlist[currentpointer][1]
        
        linkedlist[previouspointer][1] = freelist
        return True 
print(linkedlist)
addnode()
print(linkedlist)