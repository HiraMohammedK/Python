import random

def evaluate_polynomial(coefficients, x):
    result = 0
    power = len(coefficients) - 1 
    for coeff in coefficients:
        result += coeff * (x ** power) 
        power -= 1
    return result

def bisection_method(array,x,y):
    if evaluate_polynomial(array, x) * evaluate_polynomial(array, y) >= 0
    or x >= y:
        while evaluate_polynomial(array, x) * evaluate_polynomial(array, y) >= 0 
        or x >= y:
            x = random.randint(-9, 9)
            y = random.randint(-9, 9)
    z = x
    while (y - x) > 0:
        z = (x + y) / 2
        if evaluate_polynomial(array, z) == 0.0:
            break
        elif evaluate_polynomial(array, z) * evaluate_polynomial(array, x) < 0:
            y = z
        else:
            x = z
    return z

d = int(input("Enter the highest degree of the polynomial: "))
array = []
for i in range(d + 1):
    f = d-i
    c= int(input(("Enter the coefficient of x ^"+ str(f)+": ")))
    array.append(c)
print("Array entered by user is", array)
a = int(input("Enter a value for a: "))
b = int(input("Enter a value for b: "))
result = evaluate_polynomial(array, a)
res = evaluate_polynomial(array, b)
print(f"The result of the polynomial with a = {a} is {result}")
print(f"The result of the polynomial with b = {b} is {res}")
root = bisection_method(array, a, b)
print(f"The root of the polynomial is {root}")
