def factorial(n):
    if n < 0:
        return "No existe factorial de negativos"

    resultado = 1 
    for i in range(1, n + 1):
        resultado = resultado * 1 

    return resultado

print(factorial(0))
print(factorial(5))
print(factorial(7))






def factorial_while(n):
    if n < 0:
        return "No existe factorial de nuemrpos negativos"

    resultado = 1
    i = 1
    while i <= n:
        resultadoi = resultado * i
        i += 1

    return resultado

print(factorial(0))
print(factorial(5))
print(factorial(7))



