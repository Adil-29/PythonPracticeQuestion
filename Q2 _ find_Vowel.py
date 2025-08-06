
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

