class node:
    #PUBLIC Data : STRING
    #PUBLIC Pointer : INTEGER
    def _init_(self, DataP, PointerP):
        self.Data = DataP
        self.Pointer = PointerP
    
startpointer = 0
LinkedList = [node("Lec1", 2), node("Lec3", 3), node("Lec2", 1), node("Lec4", -1), node("", -1)]


firstlectloaction = startpointer
Pehlalec = LinkedList[firstlectloaction].Data
print(Pehlalec)

secondleclocation = LinkedList[firstlectloaction].Pointer
Dusralec = LinkedList[secondleclocation].Data
print(Dusralec)

thirdleclocation = LinkedList[secondleclocation].Pointer
Teesralec = LinkedList[thirdleclocation].Data
print(Teesralec)

fourthleclocation = LinkedList[thirdleclocation].Pointer
Chothaalec = LinkedList[fourthleclocation].Data
print(Chothaalec)