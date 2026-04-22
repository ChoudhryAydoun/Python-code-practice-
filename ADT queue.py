#DECLARE Names : ARRAY[0:9] OF STRING
Names = [""] * 10
HeadPointer = -1
TailPointer = 0  # Used for adding the value in the line
# ADDITION IN THE QUEUE (Tailor Bhai)  ( Tail Rear End)
def Enqueue(Data):
    global Names
    global HeadPointer
    global TailPointer

    if TailPointer < 10:
        Names[TailPointer] = Data
        TailPointer = TailPointer + 1

        if HeadPointer == -1:
            HeadPointer = 0
    else:
        print("Queue is full")

def Dequeue():
    global Names
    global HeadPointer
    global TailPointer

    if HeadPointer == -1:
        print("Queue is Empty")
    else:
        item = Names[HeadPointer]
        print(item)
        HeadPointer = HeadPointer + 1
    
    #Initialization Condition
    #So your Queue can be used Again

    if HeadPointer == TailPointer:
        TailPointer = 0
        HeadPointer = -1
Enqueue("Chup")
Enqueue("chap")
Enqueue("Parhaen")
Enqueue("Rude")
Enqueue("Egoistic")
Enqueue("Unfunny")
Enqueue("Thande")
Enqueue("Ghussa")
Enqueue("Lambi")
Enqueue("Taha")
Dequeue()
Dequeue()
Dequeue()
Dequeue()
Dequeue()
Dequeue()
Dequeue()
Dequeue()
Dequeue()
Dequeue()
Enqueue("Banoooooooooo")


print("Haider Bhai:", HeadPointer)
print("Tailor Bhai:", TailPointer)
print(Names)