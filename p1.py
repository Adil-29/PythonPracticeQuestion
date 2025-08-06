### Question 1: Sum of Elements in a List
Write a Python function that takes a list of numbers and returns the sum of all elements using a loop (not sum()).

**Sample Inputs and Outputs:**
1. Input: `[1, 2, 3, 4]` → Output: `10`
2. Input: `[0, 0, 0]` → Output: `0`
3. Input: `[-1, -2, 3]` → Output: `0`
4. Input: `[10]` → Output: `10`
5. Input: `[]` → Output: `0`

---

### Question 2: Count Occurrences in a List
Write a Python function that takes a list and an element, and returns how many times the element appears in the list using a loop.

**Sample Inputs and Outputs:**
1. Input: `[1, 2, 2, 3], 2` → Output: `2`
2. Input: `["a", "b", "a", "c"], "a"` → Output: `2`
3. Input: `[1, 1, 1], 1` → Output: `3`
4. Input: `[4, 5, 6], 7` → Output: `0`
5. Input: `[], 5` → Output: `0`

---

### Question 3: Create a Dictionary from Two Lists
Write a Python function that takes two lists (keys and values) of equal length and creates a dictionary using a loop.

**Sample Inputs and Outputs:**
1. Input: `["a", "b", "c"], [1, 2, 3]` → Output: `{"a": 1, "b": 2, "c": 3}`
2. Input: `["x", "y"], [10, 20]` → Output: `{"x": 10, "y": 20}`
3. Input: `[], []` → Output: `{}`
4. Input: `["name"], ["Alice"]` → Output: `{"name": "Alice"}`
5. Input: `["p", "q", "r"], [0, 0, 0]` → Output: `{"p": 0, "q": 0, "r": 0}`

---

### Question 4: Find Maximum in a Nested List
Write a Python function that uses nested loops to find the maximum number in a nested list (list of lists).

**Sample Inputs and Outputs:**
1. Input: `[[1, 2], [3, 4], [5, 6]]` → Output: `6`
2. Input: `[[-1, -2], [-3, -4]]` → Output: `-1`
3. Input: `[[10], [20], [30]]` → Output: `30`
4. Input: `[[1, 2, 3]]` → Output: `3`
5. Input: `[[0, 0], [0, 0]]` → Output: `0`

---

### Question 5: Merge Two Dictionaries
Write a Python function that merges two dictionaries using a loop. If a key exists in both, sum their values.

**Sample Inputs and Outputs:**
1. Input: `{"a": 1, "b": 2}, {"b": 3, "c": 4}` → Output: `{"a": 1, "b": 5, "c": 4}`
2. Input: `{"x": 10}, {"y": 20}` → Output: `{"x": 10, "y": 20}`
3. Input: `{}, {}` → Output: `{}`
4. Input: `{"p": 5}, {"p": 5}` → Output: `{"p": 10}`
5. Input: `{"a": 1, "b": 2, "c": 3}, {"a": 4}` → Output: `{"a": 5, "b": 2, "c": 3}`

---

### Question 6: Transpose a Matrix (List of Lists)
Write a Python function that transposes a matrix (list of lists) using nested loops.

**Sample Inputs and Outputs:**
1. Input: `[[1, 2], [3, 4]]` → Output: `[[1, 3], [2, 4]]`
2. Input: `[[1, 2, 3], [4, 5, 6]]` → Output: `[[1, 4], [2, 5], [3, 6]]`
3. Input: `[[1]]` → Output: `[[1]]`
4. Input: `[[1, 2], [3, 4], [5, 6]]` → Output: `[[1, 3, 5], [2, 4, 6]]`
5. Input: `[[0, 0], [0, 0]]` → Output: `[[0, 0], [0, 0]]`

---

### Question 7: Dictionary Key-Value Swap
Write a Python function that swaps keys and values in a dictionary using a loop. Assume values are unique.

**Sample Inputs and Outputs:**
1. Input: `{"a": 1, "b": 2}` → Output: `{1: "a", 2: "b"}`
2. Input: `{"name": "Alice", "age": 25}` → Output: `{"Alice": "name", 25: "age"}`
3. Input: `{}` → Output: `{}`
4. Input: `{"x": 0}` → Output: `{0: "x"}`
5. Input: `{"p": "q", "r": "s"}` → Output: `{"q": "p", "s": "r"}`

---

### Question 8: Flatten a Nested List
Write a Python function that flattens a nested list into a single list using nested loops.

**Sample Inputs and Outputs:**
1. Input: `[[1, 2], [3, 4]]` → Output: `[1, 2, 3, 4]`
2. Input: `[[1], [2], [3]]` → Output: `[1, 2, 3]`
3. Input: `[[]]` → Output: `[]`
4. Input: `[[0, 0], [0]]` → Output: `[0, 0, 0]`
5. Input: `[[1, 2, 3], [4, 5]]` → Output: `[1, 2, 3, 4, 5]`

---

### Question 9: Count Words in a List of Sentences
Write a Python function that takes a list of strings (sentences) and returns a dictionary with word counts using nested loops.

**Sample Inputs and Outputs:**
1. Input: `["hello world", "hello python"]` → Output: `{"hello": 2, "world": 1, "python": 1}`
2. Input: `["a a", "a b"]` → Output: `{"a": 3, "b": 1}`
3. Input: `[]` → Output: `{}`
4. Input: `["test test test"]` → Output: `{"test": 3}`
5. Input: `["hi", "hi there"]` → Output: `{"hi": 2, "there": 1}`

---

### Question 10: Nested Loop Pattern
Write a Python function that generates a list of lists where each inner list contains numbers from 1 to n, repeated n times, using nested loops.

**Sample Inputs and Outputs:**
1. Input: `3` → Output: `[[1, 2, 3], [1, 2, 3], [1, 2, 3]]`
2. Input: `2` → Output: `[[1, 2], [1, 2]]`
3. Input: `1` → Output: `[[1]]`
4. Input: `4` → Output: `[[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]`
5. Input: `0` → Output: `[]`

---

These questions cover a range of operations with lists, dictionaries, and nested loops. You can implement these functions and test them with the provided inputs to verify the outputs. Let me know if you'd like solutions or hints for any of these!