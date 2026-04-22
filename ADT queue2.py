#DECLARE QueueArray : ARRAY[0:9] OF STRING
QueueArray = [""] * 10
HeadPointer = 0
TailPointer = 0
NumberItems = 0

def Enqueue(InputData):
    global QueueArray
    global HeadPointer
    global TailPointer
    global NumberItems

    if NumberItems >= 10:
        return False
    else:
        QueueArray[TailPointer] = InputData
    
    # Now you are just suppose to fix your Pointers

    if TailPointer >= 9:
        TailPointer = 0
    else:
        TailPointer = TailPointer + 1
    
    NumberItems = NumberItems + 1
    return True


def Dequeue():
    global QueueArray
    global HeadPointer
    global TailPointer
    global NumberItems

    if NumberItems == 0:
        return "FALSE"
    else:
        value = QueueArray[HeadPointer]
        QueueArray[HeadPointer] = ""
        HeadPointer = HeadPointer + 1

        if HeadPointer > 9:
            HeadPointer = 0
        
        NumberItems = NumberItems - 1
        return value
Enqueue("Taha")
Enqueue("Bano")
Enqueue("Adeeba")
Enqueue("MushkeZehra")
Enqueue("Arham")
Enqueue("Sami")
Enqueue("Vivek")
Enqueue("Haider")
Enqueue("Eman")
Enqueue("Roman")
print(Dequeue())
Enqueue("Ayesha")
print(Dequeue())
print(Dequeue())
print(Dequeue())
print(Dequeue())
print(Dequeue())
print(Dequeue())
print(Dequeue())
print(Dequeue())
print(Dequeue())
print(Dequeue())




print("The TailPointer:", TailPointer)
print("The HeadPointer:", HeadPointer)
print("The Number Of Items:", NumberItems)
print(QueueArray)