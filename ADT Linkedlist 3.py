#Lecture 1 addnode
class node:
    #PUBLIC Data : INTEGER
    #PUBLIC nextNode : INTEGER
    def __init__(self, DataP, nextP):
        self.Data = DataP
        self.nextNode = nextP
    
# DECLARE linkedList : ARRAY[0:9] OF node
linkedList = [node(1, 1), node(5, 4), node(6, 7), node(7, -1), node(2, 2), 
               node(0, 6), node(0, 8), node(56, 3), node(0, 9), node(0, -1)]
startPointer = 0
emptyList = 5

def addNode(currentpointer):# if you donot want to put cuurentpointer as as prameter you can put
#(global startpointera after global emptylist) then 
#(currentpointer = startpointer)
#(C.P ko isliye letay hai so that ek copy ban jai S.P ki because after increment you will not get S.P index again so increment on copy of S.P which is C.P) )
    global linkedList
    global emptyList
    #global startPointer
    data = int(input("Enter the data to add: "))

    #STEP1 : Check if Array is full or not 
    if emptyList < 0:
        return False
    else: # ((meri ek mistake jo thi wo thi else kai ander sara code likhna hai)) 
        #STEP2 : Make a temp variable free list
        freeList = emptyList
        #STEP3 : Increment the value of emptylist so we can add a new node afterwards 
        emptyList = linkedList[emptyList].nextNode
        #STEP4 : Create a node at index postion freeList
        newNode = node(data, -1)
        linkedList[freeList] = newNode       
        #STEP5 : Find the last node index value
        previouspointer = 0
        while currentpointer != -1:
            previouspointer = currentpointer
            currentpointer = linkedList[currentpointer].nextNode       
        #STEP6 : Create connection (going on to the last node and now changing the pointer so it becomes second last node)
        linkedList[previouspointer].nextNode = freeList
        return True
addNode(startPointer)
for x in range (len(linkedList)):
    print( linkedList[x].Data , linkedList[x].nextNode )# isme loop sai karna tha and x dalna bohot zaruri hai