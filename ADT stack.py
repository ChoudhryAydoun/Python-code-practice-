#DECLARE StackData : ARRAY[0:9] OF INTEGER
#DECLARE StackPointer : INTEGER
global StackData
global StackPointer
StackData = [0] * 10
StackPointer = 0

def PrintArray():
    global StackData  #use global on everynew function
    global StackPointer

    print("The StackPointer", StackPointer)

    for x in range(10):
        print(StackData[x])

def Push(number):
    global StackData
    global StackPointer
    
    if StackPointer > 9:
        return False  #whenever returning something donot use string type type the variable or boolean as it is 
    else:
        StackData[StackPointer] = number
        StackPointer = StackPointer + 1  #it was +1 not -1
        return True

for x in range(11):
    num = int(input("Enter the number: "))
    if Push(num) == True: #Push function uses num and if true so print msg
        print("Successfully Added")
    else:
        print("The Stack Is Full") 
PrintArray()

def Pop():
    global StackData
    global StackPointer

    if StackPointer == 0:
        return -1
    else:
        StackPointer = StackPointer - 1
        Dataitem = StackData[StackPointer]
        return Dataitem
##########################################################    


