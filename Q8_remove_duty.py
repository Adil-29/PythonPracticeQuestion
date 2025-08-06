
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
