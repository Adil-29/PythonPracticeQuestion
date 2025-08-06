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
