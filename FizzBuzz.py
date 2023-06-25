"""
- For numbers divisible by 3, print "Fizz" instead of the number
- For numbers divisible by 5, print "Buzz" instead of the number
- For numbers divisible by both 3 and 5, print "FizzBuzz" instead 
"""


def fizz_buzz(value):
    result = ''
    c = 0
    for i in range(1, value+1):
        pattern = [i, i,'Fizz', i, 'Bizz', 'Fizz', i, i, 'Fizz', 'Bizz', i, 'Fizz', i, i,  'FizzBizz']
        result += f' {pattern[c]}'
        c += 1
        if c == 15:
            c = 0
    return result


print(fizz_buzz(31))
