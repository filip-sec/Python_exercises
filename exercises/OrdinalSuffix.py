def ordinalSuffix(number):
    numberStr = str(number)

    if numberStr[-2:] in('11', '12', '13'):
        return numberStr + "th"
    if numberStr[-1] == '1':
        return numberStr + 'st'
    if numberStr[-1] == '2':
        return numberStr + 'nd'
    if numberStr[-1] == '3':
        return numberStr + 'rd'
    return numberStr + 'th'


# Test cases
print(ordinalSuffix(0))    # Output: 0th
print(ordinalSuffix(1))    # Output: 1st
print(ordinalSuffix(2))    # Output: 2nd
print(ordinalSuffix(3))    # Output: 3rd
print(ordinalSuffix(4))    # Output: 4th
print(ordinalSuffix(10))   # Output: 10th
print(ordinalSuffix(11))   # Output: 11th
print(ordinalSuffix(12))   # Output: 12th
print(ordinalSuffix(13))   # Output: 13th
print(ordinalSuffix(14))   # Output: 14th
print(ordinalSuffix(101))  # Output: 101st