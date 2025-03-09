# # operators task -1....
# #area of rectangle .....1
# length = int(input("enter the rectangle length :" ))
# width = int(input("enter the width of rectangle :"))
# area = length * width #area of rectangle
# print(f"given rectangle length is {length} and the width is {width} and then area of rectangle is {area}")

# #incrementing and decrementing variables .......2
# num = 20
# num +=5
# print(num)
# num -=10
# print(num)

# #convert temperature fron celicius to farenheat ........3
# celcius = int(input("enter the celcius temperature :"))
# farenheat = (celcius * 9/5) +32
# print(f"given celcius temperature is converted into farenheat is {farenheat} temperature")

# # the simple interest given the principle amount, rate, and time (in years).....4
# principle_amount = 100000
# interest = 1
# time = 2 * 12
# result = ( principle_amount * interest/100 ) * time
# print(f"given priciple amount is {principle_amount} to gives to the person and then the duration is {time} months or 2 years then the interest can be generated {result} ")

# #concatenate two strings and display the result. The strings should be taken as input from the user....5
# num = (input("enter the first number :"))
# num += (input("enter the second number :"))
# print(num)

# #convert a distance from kilometers to miles.....6
# distance = int(input("enter the kilometers :"))
# mile = 0.6 
# result = distance * mile
# print(f"the given distance is {distance} kilometers is equal to {result} miles ")

# # Exercise: Create a program that takes user input for their name and age. Use formatted strings (f-strings) to print a message welcoming the user 
# #.......operators task -2 .......1
# user_name = str(input("enter the  the user name :"))
# age = int(input("enter the age :"))
# print(f"welcoming the user {user_name} are you old of {age} years ")

# # formatted strings to display the information in a readable format ...2
# dictionary_1 = {
#    " product" : "milk" , 
#     "price" : "15" , 
#     "quantity" : "25"

# }
# print(f"this shop consist of {dictionary_1}")

# #Check if the number 5 is in the list.
# # Check if the number 15 is not in the list .......3
# list_1 = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
# print(5 in list_1)
# print(15 in list_1)

#-----------------------------------------------------------------
# #control statment tasks 
# #vowel Checker:
# char = input("enter the vowel :")
# vowels = ["a" , "e" , "i" , "o" , "u"] 
# if char in vowels :
#     print(f"{char} is vowels")
# else :
#     print("it is not a vowel")

# # Age Group Classification
# age = int(input("enter the age :"))
# if age <= 12 :
#     print(f"the  age is  {age} he/she is a child")
# elif age <= 17 :
#     print(f"the age is {age} he/she is a teenagers")
# elif age <= 64 :
#     print(f"the age is {age} he/she is a adults ")
# else  :
#     print(f"the age is {age >= 65} he/she is a senior citizens")

# #Number Classifier:
# num = int(input("enter the number :"))
# if num>0 :
#     print(f"number {num} is positive")
# elif num<0 :
#     print(f"number {num} is negative")
# else :
#     print("number is zero") 


# # Leap Year Checker:
# year = int(input("enter the year :"))
# if year % 4 == 0 and year % 100 ==0 or year % 400 == 0 :
#     print(f"year {year} is leap year")
# else :
#     print("it is not leap year")

# #Calculator:
# num = int(input("enter the first number :"))
# num_1 = int(input("enter the second number :"))
# result = num + num_1 , num - num_1 , num * num_1 , num / num_1
# print(result)

# # Short Hand If:
# x = 6
# result = (f"the number {x} is even") if x % 2 == 0 else ("the number is odd " )
# print (result)
    
# #Discount Calculator:
# price = int(input("enter the original price :"))
# discount = int(input("enter the discount :"))
# result = price * discount/100
# final_price = price - result
# print(f"the total price is {price} and the dicount is {discount} after the discount the final price is {final_price} ")

# # BMI Calculator:
# weight = int(input("enter the weight :"))
# height = int(input("enter the height :"))
# result = weight / height
# print(f"the weight is {weight} and the height is {height} and then we get {result}")




    





