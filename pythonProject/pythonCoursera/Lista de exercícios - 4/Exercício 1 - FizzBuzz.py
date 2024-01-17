def fizzbuzz (x):
    if x % 3 == 0 and x % 5 != 0:
        m = 'Fizz'
    elif x % 5 == 0 and x % 3 != 0:
        m = 'Buzz'
    elif x % 3 == 0 and x % 5 == 0:
        m = 'FizzBuzz'
    else:
        m = x

    return m


print(fizzbuzz(3))