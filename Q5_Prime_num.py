5. Check if a Number is Prime
Problem: Write a function that checks if a given number is prime (divisible only by 1 and itself).
Sample Inputs and Outputs:

Input: 7 → Output: True (prime)
Input: 4 → Output: False (divisible by 2)
Input: 1 → Output: False (1 is not prime)
Input: 13 → Output: True (prime)
Input: 15 → Output: False (divisible by 3, 5)





x = int (input("Number"))
count = 0
divisors =[]
for i in range (1, x+1):
    if x % i == 0:
        count += 1
        divisors.append(i)
if count == 2:
        print(True, "Prime number")
else:
    print(False, "Not prime number",x, "is divisible by =" , divisors)
