4. Reverse a List
Problem: Write a function that reverses a given list without using the built-in reverse() method or slicing.
Sample Inputs and Outputs:

Input: [1, 2, 3, 4] → Output: [4, 3, 2, 1]
Input: ["a", "b", "c"] → Output: ["c", "b", "a"]
Input: [] → Output: [] (empty list)
Input: [5] → Output: [5] (single element)
Input: [1, "hello", 3.14] → Output: [3.14, "hello", 1]


def reverse_list(lst):
    reversed_list = []
    for item in lst:
        reversed_list.insert(0, item)  # Add each item at the start
    return reversed_list

# Example usage:
nums = [1, 2, 3, 4, 5]
print(reverse_list(nums))