# Global vs Local Scope
# Anything that is in global scope can not be used inside local scope 
# What exactly is Local scope 
# Local scope is anything which is inside function/procedure  (Bhabhi Room)
# Global scope is anything which is outside function/procedure (Ghar)
# Parameters can be passed in two ways 
# By value parameters and By reference parameters
# In python we don't have by ref paramater passing 
# We can only pass by value 
Result = "C"
# We dont have parameter by ref so we are using global for that
def ChangeResult():
    global Result
    if Result == "C":
        Result = "A*"
    
    print("Testing Inside Function Result:", Result)

ChangeResult()

print("Actual result Outside Function:", Result)
# jab bhi ap parameter pass karte ho as by val to its like making
# a photocopy of the result and making changes on a photocopy instead of
# the actual result 
# actual result does not change why because changes sirf 
# ek photocopy per ho rahe hein
# To Bhai Phir Kia Karen 
# The right approach is to use by ref parameter 
# SAD News or maybe good (We dont have by ref in python)
# We do jugar 
# use global keyword

