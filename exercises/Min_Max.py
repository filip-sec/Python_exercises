def getSmallest(numbers):
    if len(numbers) == 0:
        return None
    
    smallest = numbers[0]

    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

assert getSmallest([1, 2, 3]) == 1
print(getSmallest([1, 2, 3]))
assert getSmallest([3, 2, 1]) == 1
print(getSmallest([3, 2, 1]))
assert getSmallest([28, 25, 42, 2, 28]) == 2
print(getSmallest([28, 25, 42, 2, 28]))
assert getSmallest([1]) == 1
print(getSmallest([1]))
assert getSmallest([]) == None
print(getSmallest([]))
