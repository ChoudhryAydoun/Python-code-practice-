'''try:
    num = int(input ("enter the number "))
    print(num)
except ValueError:#valueerror meansd when wrong data type is entered
    print("wrong input write integer value")
#see after all error dure to exception the other statemnts are getting executed if exception was not present than they would not.  
print("HEllo taha") 
print("Aydoun")
#2
try:
    num = int(input("Enter the number"))
    print(5/num)
except ZeroDivisionError:
    print("value cannot be divided by zero")'''


'''hamri ek galti ho rahi thi sir sai kai unho nai pehle valueError diya tha code mai but usme w value eroor and zerodivision error 
dono ka samjha rahay thay but wo error de raha tha kiyu kai wo zerodivision error bhi valuerror sai hi solve hojana tha '''


# In paper abhi tak sirf IO exception hi ai hai valueeroor and zerodivision error is extra knowledge but paper mai if file is given
#so lazmi use IO exception and use karna like mainay kiya hai nechay bholna nahi hai use karna.
try:
    file = open("hellokity.txt","r")
    print(file.read())
    file.close() #close lazmi karna hai i forgot to do
except IOError :
    print("File doesnot exist")

