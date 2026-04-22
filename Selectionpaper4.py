#Question num 1
number1 = float(input("Enter the number1 :"))
number2 = float(input("Enter the number2 :"))
number3 = float(input("Enter the number3:"))

if number1 > number2 and number1 > number3 :
   print (number1, "is the largest ")
elif number2 > number1 and number2 >number3:
   print (number2 ,"is the largest")
else :
   print (number3, "is the largest ")


#Question num 2 
Password = input("Enter the password:")
mail = input("Enter the email:")
if Password == ("12ab") and mail==("123@papersdock.com"):
   print ("Correct email and password")
else:
   print ("Wrong email and password")

