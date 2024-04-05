def fizzBuzz(upTo):
    for num in range(1, upTo + 1):
        if num % 5 == 0:
            print("Buzz", end=' ')
        elif num % 3 == 0:
           print("Fizz", end=' ')
        elif num % 3 == 0 and num % 5 == 0:
            print("fizzBuzz", end=' ')
        else:
            print(num, end=' ')

# Test the function with a limit of 15
fizzBuzz(15)