Question 1: 
Sum of Numbers in a List
   # Write a function that takes a list and returns the sum of all elements.

x = []
n = int(input("Enter Numbers in list"))
for i in range (n):
    num= int(input("number"))
    x.append(num)
def sum_list(x):
    total = sum(x)
    return total
print("Sum List:" , sum_list(x))    


   

Question 2: 
Find Max in List
   # Without using max(), find the largest number in a list.	
   
# Question 2: 
# Find Max in List
#   # Without using max(), find the largest number in a list.
x = []
n = int(input("Enter total numbers in list"))
for i in range(n):
    num = int(input("Number"))
    x.append(num)
def max_num(x):
    max_num = x[0]
    for num in x:
        if num > max_num:
         max_num = num
    return max_num
print("Maximum num in list is :" , max_num(x))


Question 3: 
Count Even and Odd Numbers in a List
   # Create a function that counts even and odd numbers in a given list.

x = []
n = int(input("Total numbers in list"))
for i in range(n):
    num = int(input("Number"))
    x.append(num)
def even_odd(x):
    even_count = 0
    odd_count = 0
    for num in x:
        if num % 2 == 0:
            even_count += 1
        else:    
            odd_count += 1
    return even_count, odd_count 
y = even_odd(x)    
# even_count , odd_count = even_odd(x)
# print("Number is Even:" , even_count)
# print("Number is Odd:" , odd_count)
print("Number is Even:" , y[0])
print("Number is Odd:" , y[1])
   

Question 4: 
Reverse a List
   # Create a function to reverse a list manually (without using reverse()).
x= []
n = int(input("enter numbers in list"))
for i in range (n):
    num = int(input("Number"))
    x.append(num)
def reverse_list(x):
    reverse_lst = []
    for i in range (len(x)-1,-1,-1):
        reverse_lst.append(x[i])
    return reverse_lst
print("reverse list:", reverse_list(x))           


Question 5: 
Check if Number is Prime
   # Ask user to input a number, and check if it is prime.
   x = int(input("Enter Number"))
count = 0
for i in range (1, x +1):
    if x % i == 0:
        count +=1
if count ==2:
    print ("prime number")
else:
    print ("It is not prime number")




Question 6: 
List of Prime Numbers
	# Write a function that returns all prime numbers between 1 and 100.


for num in range (1, 100):
    count = 0
    for x in range (1, num+1):
        if num % x == 0:
            count += 1
    if count == 2:
     print(num,"it is prime number")
    else:
       print(num,"it is not prime number")

Question 7: 
Simple Password Validator
	# Ask the user for a password.
	# Validate:
	# - At least 8 characters
	# - Contains both letters and numbers
	# - Does not contain spaces

# Question 7: 
# Simple Password Validator
# Ask the user for a password.
# Validate:
# At least 8 characters
# Contains both letters and numbers
# Does not contain spaces
password = input("Enter Password")
if len(password) < 8:
    print ("Password must be 8 characters")
elif password.isalpha():
    print("Password must contain digit")
elif password.isdigit():
    print("Password must contain letters")
elif " " in password:
    print ("Password should not contain spaces")
else:
    print ("Valid password")
        
Question 8: 
Find Duplicate Elements in List
	# Return all elements that appear more than once in a list.

x = []
n = int(input("Numbers in list"))
for i in range(n):
    num = int(input("Number"))
    x.append(num)
# x = [1,2,2,2,3,3,4,5]
def duplicate_list(lst): 
    duplicate = []
    for num in lst:
        if lst.count(num) > 1 and num not in duplicate:
            duplicate.append(num)
    return(duplicate)
result = duplicate_list(x)
print("duplicate elements in list", result)




Question 9: 
FizzBuzz
	# For numbers from 1 to 50:
	# - Print "Fizz" for multiples of 3
	# - Print "Buzz" for multiples of 5
	# - Print "FizzBuzz" for both
	# - Else print the number

x = int(input("Enter Number"))
if x % 3 == 0 and x % 5 == 0:
    print ("Fizz Buzz")
elif x % 3 == 0:
    print ("Fizz")
elif x % 5 == 0:
    print ("Buzz")
else:
    print("Number", x)


Question 10: 
Find the Sum and Average
# Given a list of numbers, calculate and return the sum and average.
x = []
count = 0
total = 0
n = int(input("enter total numbers in list"))
for i in range(n):
    num = int(input("Number"))
    x.append(num)
for i in (x):
  total += i
  count += 1
average = total/count  
print("Sum of numbers" , total)  
print("Average of list" , average)

