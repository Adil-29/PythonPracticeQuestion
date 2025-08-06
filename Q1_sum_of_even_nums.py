
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
