class node:
    #PUBLIC Data : INTEGER
    #PUBLIC nextNode : INTEGER

    def __init__(self, DataP, nextP):
        self.Data = DataP
        self.nextNode = nextP
    
# DECLARE linkedList : ARRAY[0:9] OF node
linkedList = [node(1, 1), node(5, 4), node(8, 7), node(70, -1), node(6, 2), 
              node(0, 6), node(0, 8), node(56, 3), node(0, 9), node(0, -1)]

startPointer = 0
emptyList = 5

def OutputNodes():
    global linkedList
    global startPointer
    currentpointer = startPointer
    while currentpointer != -1:
        datanode = linkedList[currentpointer].Data
        print(datanode)
        currentpointer = linkedList[currentpointer].nextNode

def deleteNode():
    global linkedList
    global emptyList
    global startPointer

    currentpointer = startPointer
    datatodelete = int(input("Enter the data to delete: "))

    #STEP1 : Find the index position of the data that you want to delete 
    previouspointer = 0
    while currentpointer != -1 and linkedList[currentpointer].Data != datatodelete:
        previouspointer = currentpointer
        currentpointer = linkedList[currentpointer].nextNode
    
    if currentpointer == -1:
        # it means that the data that you want to find does not exist
        return False
    else:
        #STEP2 Pointer Connection
        #Case1: First node is to be deleted (increment startpointer)
        #Case2: Middle/End node is to be deleted (change previous node)
        if currentpointer == startPointer:  #it is case 1
            startPointer = linkedList[startPointer].nextNode
        else:
            linkedList[previouspointer].nextNode = linkedList[currentpointer].nextNode #it is case 2
        
        #STEP3 Adding the removed node in emptylist
        linkedList[currentpointer].Data = 0
        linkedList[currentpointer].nextNode = emptyList
        emptyList = currentpointer
        return True
    
