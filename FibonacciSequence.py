"""
Fibonacci sequence: 
Create a program that generates the Fibonacci sequence up to a certain number entered by the user.
"""


def fibonacci(number):
    result = [0, 1]
    for i in range(number):
        result.append(result[-1] + result[-2])
    return result[:-1]


print(fibonacci(0))