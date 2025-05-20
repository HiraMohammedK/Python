def evaluate_polynomial(coefficients, x):
    result = 0
    power = len(coefficients) - 1
    for coeff in coefficients:
        result += coeff * (x ** power)
        power -= 1
    return result

def newton_raphson(x,array,coeff):
    h = evaluate_polynomial(array, x) / evaluate_polynomial(coeff, x)
    while abs(h) >= 0.0001:
        h = evaluate_polynomial(array, x) / evaluate_polynomial(coeff, x)

        # x(i+1) = x(i) - f(x) / f'(x)
        x = x - h

    print("The value of the root is : ",                        
    "%.4f"% x)

d = int(input("Enter the highest degree of the polynomial: "))
array = []
for i in range(d + 1):
    f = d - i
    c = int(input("Enter the coefficient of x ^"+str(f)+" : "))
    array.append(int(c))
print("Enter the coefficiants of derivative : ")
coeff = []
for i in range(d):
    f = d - i - 1
    c = int(input("Enter the coefficient of x ^"+str(f)+" : "))
    coeff.append(c)
i = int(input("Enter the initial guess: "))
newton_raphson(i,array,coeff)
