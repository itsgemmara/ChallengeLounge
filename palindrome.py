"""
Here's a challenge for you:

Write a Python program that takes a user input string and checks if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.

Example:
Input: "racecar"
Output: "Yes, it is a palindrome"

Input: "hello"
Output: "No, it is not a palindrome"

You can use any method you prefer to check if the input string is a palindrome. Good luck!
"""


def check_palindrome(user_input):
    user_input = str(user_input).lower().replace(' ', '')
    mid_idx, right_start_idx = len(user_input)//2 , len(user_input)//2 
    if len(user_input) % 2 != 0:
        right_start_idx = mid_idx + 1
    left = user_input[:mid_idx]
    right = user_input[right_start_idx:] 
    c = 0
    while right[c] == left[len(left) - c - 1]:
        c += 1
        if c == len(left): 
            return True
    return False


def check_palindrome2(user_input):
    user_input = str(user_input).lower().replace(" ", "")
    return user_input == user_input[::-1]


print(check_palindrome2('Step on no pets'))