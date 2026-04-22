Names = ["Taha","Ahmed","Pappu","Bano","Banto","Pappu"]

 # TO acces alll the data from an (array/list)
for x in range(len(Names)):
    print (Names[x])

for x in range (len(Names)):
    if Names[x] == "Bano":
        print("The value is:",x)

#Q1 Input a name from the User if that
# name is in array then print it is already there and if not in the array then add it into the array ? 
# point :if we want efficeinet then use whileloop if dont then forloop. never do apppend command in a loop.

newname = input("enter the name :")
flag = False
for x in range (len(Names)):
    if Names[x] == newname:
        flag = True

if flag == False:
    Names.append (newname)
else:
    print ("already there")
    
print(Names)

#Q2 Numbers = [ 10, 32, 24, 56, 75, 86], Reverse the Order of the array [86, 75, 56, 24, 32, 10],num = [ 10, 32, 24, 56, 75, 86]

Numbers = [ 10, 32, 24, 56, 75, 86]
newnum = [0 , 0 ,0 , 0, 0 , 0]
oppositeindex = 5 
for i in range(len(Numbers)):
    newnum[i] = Numbers[oppositeindex]
    oppositeindex = oppositeindex - 1

print (newnum)

#Q3 Ask Numbers form the user and find the average of those number and when the user types in 0 then stop asking the
# number from the user and print the average ,Note : 0 should not be considered a number 

sum =0 
count = 0 
flag = True 
while flag == True:
    num = float(input("enter the num:")) 
    if num == 0:
        flag = False 
    else:
        sum = sum + num 
        count = count + 1 
        avg = sum /count         
print (avg)

################### 2D Array ########################
array = [[3,0,6,0,5,0],[0,0,0,0,0,0],[10,20,40,50,60,70]]
print (array[2][2])


for rows in range(2): #it was total 3 you must put one num less in both row and col only for arrays  not in funtion
    for col in range (5): # it was total 6
        print(array[rows][col])

##q1 There is a 2D array print "Present if "Faisal" is in the array.

array2d = [["Ahmed" , "ALi" , "bano"],["Qasim" , "Faisal" , "khalid"]]
for rows in range(2):
    for col in range (3):
        if array2d[rows][col] == "Faisal":
            print ("Present")

#1D array 
EmpArray = [""]* 500
EmpArray [2] = 44
print (EmpArray)

#2D aray 
empty = [[""]*40 for i in range(500)]
empty[2][2] = 66
print(empty)