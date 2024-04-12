def calculateSum(numbers):
    result = 0
    for number in numbers:
        result += number
        return result
     
def calculateProduct(numbers):
    result = 1
    for number in numbers:
        result *= number
        return result

assert calculateSum([]) == 0
assert calculateSum([2, 4, 6, 8, 10]) == 30
assert calculateProduct([]) == 1
assert calculateProduct([2, 4, 6, 8, 10]) == 3840