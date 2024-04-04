def convertToFahrenheit(degreeCelsius):
    return degreeCelsius * (9/5) + 32 

def convertToCelsius(degreesFarenheit):
    return (degreesFarenheit - 32) * (5/9)

# Assert statements to test the functions
assert convertToCelsius(0) == -17.77777777777778
assert convertToCelsius(180) == 82.22222222222223
assert convertToFahrenheit(0) == 32
assert convertToFahrenheit(100) == 212
assert convertToCelsius(convertToFahrenheit(15)) == 15

print("All assert statements passed successfully.")

# Rounding errors cause a slight discrepancy:
assert convertToCelsius(convertToFahrenheit(42)) == 42.00000000000001