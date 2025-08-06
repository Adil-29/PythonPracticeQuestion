
1. Sum of Even Numbers in a List
Problem: Write a function that takes a list of integers and returns the sum of all even numbers in the list.
Sample Inputs and Outputs:

Input: [1, 2, 3, 4, 5, 6] → Output: 12 (2 + 4 + 6)
Input: [1, 3, 5, 7] → Output: 0 (no even numbers)
Input: [2, 4, 6, 8] → Output: 20 (2 + 4 + 6 + 8)
Input: [] → Output: 0 (empty list)
Input: [-2, 3, -4, 5, 6] → Output: 0 (-2 + -4 + 6 = 0)

x = [1,2,3,4,5,6,7,8,9,11,12]
def even_sum(x):
    # count = 0:
    y = []	
    for i in x:
        if i % 2 == 0:
            y.append(i)
            sum_list = sum(y)
    return (y, sum_list)
list,sum_list= even_sum(x) 
print(list , sum_list)






2. Count Vowels in a String
Problem: Write a function that counts the number of vowels (a, e, i, o, u) in a given string (case-insensitive).
Sample Inputs and Outputs:

Input: "hello" → Output: 2 (e, o)
Input: "PYTHON" → Output: 1 (o)
Input: "aeiou" → Output: 5 (a, e, i, o, u)
Input: "xyz" → Output: 0 (no vowels)
Input: "HeLLo WoRLD" → Output: 3 (e, o, o)







x = "HEello Pakistan".lower()
def vowel_list(x):
    count = 0
    y = []
    for i in x:
        if i in ("a", "e", "i", "o", "u"):
            count +=1
            y.append(i)
    return (y, count)
vowel, count = vowel_list(x)
print ("Vowels are" , vowel, "Total numbers of vowels ="  ,count)

3. Find the Maximum Key in a Dictionary
Problem: Write a function that returns the key with the maximum value in a dictionary. If the dictionary is empty, return None.
Sample Inputs and Outputs:

Input: {"a": 10, "b": 20, "c": 15} → Output: "b" (20 is max)
Input: {"x": 5, "y": 5} → Output: "x" or "y" (equal max, return any)
Input: {"p": -1, "q": -5, "r": -10} → Output: "p" (-1 is max)
Input: {} → Output: None (empty dictionary)
Input: {"single": 100} → Output: "single" (only key)
x = { "q": 99, "w": 100, "r": 110}
max_value = max(x.values())
print(max_value)

4. Reverse a List
Problem: Write a function that reverses a given list without using the built-in reverse() method or slicing.
Sample Inputs and Outputs:

Input: [1, 2, 3, 4] → Output: [4, 3, 2, 1]
Input: ["a", "b", "c"] → Output: ["c", "b", "a"]
Input: [] → Output: [] (empty list)
Input: [5] → Output: [5] (single element)
Input: [1, "hello", 3.14] → Output: [3.14, "hello", 1]


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

6. Merge Two Dictionaries
Problem: Write a function that merges two dictionaries. If a key exists in both, keep the value from the second dictionary.
Sample Inputs and Outputs:

Input: {"a": 1, "b": 2}, {"b": 3, "c": 4} → Output: {"a": 1, "b": 3, "c": 4}
Input: {"x": 10}, {"y": 20} → Output: {"x": 10, "y": 20}
Input: {}, {"a": 5} → Output: {"a": 5}
Input: {"p": 1}, {} → Output: {"p": 1}
Input: {"a": 1}, {"a": 2} → Output: {"a": 2}

x = {"a" : 2, "b": 3, "c": 6}
y = {"e" : 222, "f": 322, "q": 126}
x.update(y)
print(x)



7. Count Occurrences in a List
Problem: Write a function that counts how many times a given element appears in a list.
Sample Inputs and Outputs:

Input: [1, 2, 2, 3, 2], 2 → Output: 3 (2 appears 3 times)
Input: ["a", "b", "a"], "a" → Output: 2 (a appears 2 times)
Input: [1, 2, 3], 4 → Output: 0 (4 not in list)
Input: [], 5 → Output: 0 (empty list)
Input: [1, 1, 1], 1 → Output: 3 (1 appears 3 times)

x =[1,2,3,4,5,6,6]
given_num = 1
count = 0
for i in x:
    if i == given_num:
        count+= 1
if count >= 1:        
    print(given_num, "apperas", count, "times")
else:
    print("Given number dont exixt in list")

8. Remove Duplicates from a List
Problem: Write a function that removes duplicates from a list while preserving the original order of elements.
Sample Inputs and Outputs:

Input: [1, 2, 2, 3, 1] → Output: [1, 2, 3]
Input: ["a", "b", "a", "c"] → Output: ["a", "b", "c"]
Input: [1, 1, 1] → Output: [1]
Input: [] → Output: [] (empty list)
Input: [3, 3, "x", "x", 4] → Output: [3, "x", 4]




x = [1,2,3,4,5,6,6,77,88,99,9,7,1,"a","a",2,3,4,5,2]
unique_list =set(x)
print (unique_list)
print(len(x))
print (len(unique_list))

9. Find Common Elements
Problem: Write a function that returns a list of common elements between two lists.
Sample Inputs and Outputs:

Input: [1, 2, 3], [2, 3, 4] → Output: [2, 3]
Input: ["a", "b", "c"], ["b", "d"] → Output: ["b"]
Input: [1, 2], [3, 4] → Output: [] (no common elements)
Input: [], [1, 2] → Output: [] (empty list)
Input: [1, 1, 2], [1, 2, 2] → Output: [1, 2]

x = [1,2,3,4,5]
# y = [2,4,6,7,8]
# common_list = []
# for i in x:
#     if i in y:
#         common_list.append(i)
# if len(common_list) == 0:       
#     print("No common element")
# else:
#     print("Common List", common_list)
10. Dictionary Value Sum
Problem: Write a function that returns the sum of all values in a dictionary. Assume values are numbers.
Sample Inputs and Outputs:

Input: {"a": 10, "b": 20, "c": 30} → Output: 60 (10 + 20 + 30)
Input: {"x": -5, "y": 5} → Output: 0 (-5 + 5)
Input: {} → Output: 0 (empty dictionary)	
Input: {"p": 1} → Output: 1 (single value)
Input: {"q": 2.5, "r": 3.5} → Output: 6.0 (2.5 + 3.5)
list= {
#     "a" : 9,
#     "b" : 10,
#     "c" : 11,
#     "d" : 19,
#     "e" : 20,
#     }
# total = sum(list.values())
# print("Sum of Values of keys =",total)



















Question 1: Sum of Elements in a List
Write a Python function that takes a list of numbers and returns the sum of all elements using a loop (not sum()).

**Sample Inputs and Outputs:**
1. Input: `[1, 2, 3, 4]` → Output: `10`
2. Input: `[0, 0, 0]` → Output: `0`
3. Input: `[-1, -2, 3]` → Output: `0`
4. Input: `[10]` → Output: `10`
5. Input: `[]` → Output: `0`

---
x = [1,2,3,4,5,6,7,8,9,11,12]
def even_sum(x):
    sum_list = 0
    y = []
    for i in x:
        if i % 2 == 0:
            y.append(i)
    for i in y:
        sum_list += i
    return (y, sum_list)
list,sum_list= even_sum(x) 
print(list , sum_list)
        
