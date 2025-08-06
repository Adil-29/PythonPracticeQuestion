
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

