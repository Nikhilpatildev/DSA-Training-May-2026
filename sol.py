# s = "Nikhil is a good boy"
# print(s[::-1])

# # Check for valid parentheses

# s = input("Enter brackets: ")

# stack = []

# pairs = {
#     ')': '(',
#     '}': '{',
#     ']': '['
# }

# for ch in s:
#     if ch in "({[":
#         stack.append(ch)
#     elif ch in ")}]":
#         if not stack or stack[-1] != pairs[ch]:
#             print("Invalid")
#             break
#         stack.pop()
# else:
#     if not stack:
#         print("Valid")
#     else:
#         print("Invalid")

# # find the first non-repeating character in a string
# s = input("Enter a string: ") 
# char_count = {}
# for ch in s:
#     char_count[ch] = char_count.get(ch, 0) + 1
# for ch in s:
#     if char_count[ch] == 1:
#         print("First non-repeating character: ", ch)
#         break
# else:
#     print("No non-repeating character found.")

    #inseration sort
# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#     return arr
# arr = [12, 11, 13, 5, 6]
# sorted_arr = insertion_sort(arr)
# print("Sorted array: ", sorted_arr)

# arr = [5, 3, 4, 1, 2]

# arr = [5, 3, 4, 1, 2]

# n = len(arr)

# for i in range(1, n):
#     key = arr[i]
#     j = i - 1

#     while j >= 0 and arr[j] > key:
#         arr[j + 1] = arr[j]
#         j -= 1

#     arr[j + 1] = key

# print("Sorted array:", arr)

# students = [
#     {'name': 'Amit', 'marks': 75},
#     {'name': 'Ravi', 'marks': 90},
#     {'name': 'Neha', 'marks': 60}
# ]

# students.sort(key=lambda x: x['marks'])

# print(students)

# #remove all elements from a dictionary
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# my_dict.clear()
# print(my_dict)


