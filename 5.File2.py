#Q1 write file 
'''file = open("Eventguest.txt", "w")
flag = False
while  flag == False:
    user = input("enter the name:")
    if user.lower() == "no":
        flag = True
    else:
        file.write(user + \n")
file.close()'''

#Q2 of append mode question 
file3 = open("Eventguest.txt", "r")
flag = False
for line in file3:
    if line.strip() == "Papersdock":
        flag = True
        print("already invited")
    
file4 = open("Eventguest.txt", "a")
if flag == False:
    file4.write("Papersdock\n")
file4.close()


