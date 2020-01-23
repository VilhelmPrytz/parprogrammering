def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"

    if num % 3 == 0:
        return "Fizz"
    
    if num % 5 == 0:
        return "Buzz"
    
    return num


print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(4))


