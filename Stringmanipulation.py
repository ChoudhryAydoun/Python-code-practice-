# 1 Question 
#Name = "Taha Ali"
#full = Name[0:4]
#last = Name[5:8]
#print (full)
#print (last)

# 2 Question 
# sir code of this question 
name = input("enter the name:")
firstnamelengh = 0 
i = 0 # i jo hai lazmi lagay ga iski hi galti hoti hai 
#and array bhi usehoga
flag = True 
while flag == True:
    if name[i] == " ":
     flag = False
    else:
        firstnamelengh = firstnamelengh +1 
        i = i + 1

firstname = name[0:firstnamelengh]
lastname = name [firstnamelengh+1 : len(name)]
print ("firstname is :", firstname)
print ("lastname is :", lastname)

#second mehtiod of this question which i think is better
# Declare fullName : STRING
# Declare spacePosition : INTEGER
# Declare lastName : STRING
fullName = input("Enter your full name: ")
spacePosition = 0
for x in range(len(fullName)):
    if fullName[x] == " ":
        spacePosition = x
lastName = fullName[spacePosition +1 : len(fullName)]
print("Last Name:", lastName)