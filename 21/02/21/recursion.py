def factorial(n):
    if n < 0:
        raise ValueError("No existe factorial de números negativos")
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("="*50)
print("PRUEBAS FACTORIAL")
print(factorial(0))    
print(factorial(5))
print(factorial(10))   



def factorial_for(n):
    if n < 0:
        raise ValueError("No existe factorial de números negativos")
    
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    
    return resultado

print("="*50)
print("FACTORIAL - FOR")
print(factorial_for(0))
print(factorial_for(5))
print(factorial_for(10))




def factorial_while(n):
    if n < 0:
        raise ValueError("No existe factorial de números negativos")
    
    resultado = 1
    i = 1
    
    while i <= n:
        resultado *= i
        i += 1
    
    return resultado

print("="*50)
print("FACTORIAL - WHILE")
print(factorial_while(0))
print(factorial_while(5))
print(factorial_while(10))



def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

print("="*50)
print("PRUEBAS SUMA DE DÍGITOS")
print(suma_digitos(9))      
print(suma_digitos(99))     
print(suma_digitos(1234))   
print(suma_digitos(98765))  



def suma_digitos_for(n):
    suma = 0
    for digito in str(n):
        suma += int(digito)
    return suma

print("="*50)
print("SUMA DÍGITOS - FOR")
print(suma_digitos_for(9))
print(suma_digitos_for(99))
print(suma_digitos_for(1234))



def suma_digitos_while(n):
    suma = 0
    while n > 0:
        suma += n % 10
        n //= 10
    return suma

print("="*50)
print("SUMA DÍGITOS - WHILE")
print(suma_digitos_while(9))
print(suma_digitos_while(99))
print(suma_digitos_while(1234))




def busqueda_binaria(arr, objetivo, izq, der):
    if izq > der:
        return -1
    
    medio = (izq + der) // 2
    
    if arr[medio] == objetivo:
        return medio
    elif objetivo < arr[medio]:
        return busqueda_binaria(arr, objetivo, izq, medio - 1)
    else:
        return busqueda_binaria(arr, objetivo, medio + 1, der)
    
    print(busqueda_binaria(lista, 23, 0, len(lista)-1))
    

lista = [2, 5, 8, 12, 16, 23, 38, 45, 72, 91]

print("="*50)
print("PRUEBAS BÚSQUEDA BINARIA")
print(busqueda_binaria(lista, 23, 0, len(lista)-1))  
print(busqueda_binaria(lista, 99, 0, len(lista)-1))  
print(busqueda_binaria(lista, 2, 0, len(lista)-1))  


def busqueda_binaria_for(arr, objetivo):
    for i in range(len(arr)):
        if arr[i] == objetivo:
            return i
    return -1

lista = [2, 5, 8, 12, 16, 23, 38, 45, 72, 91]

print("="*50)
print("BÚSQUEDA - FOR")
print(busqueda_binaria_for(lista, 23))
print(busqueda_binaria_for(lista, 99))



def busqueda_binaria_while(arr, objetivo):
    izq = 0
    der = len(arr) - 1
    
    while izq <= der:
        medio = (izq + der) // 2
        
        if arr[medio] == objetivo:
            return medio
        elif objetivo < arr[medio]:
            der = medio - 1
        else:
            izq = medio + 1
    
    return -1

print("="*50)
print("BÚSQUEDA - WHILE")
print(busqueda_binaria_while(lista, 23))
print(busqueda_binaria_while(lista, 99))



def es_palindromo(texto):
    texto = texto.replace(" ", "").lower()
    
    if len(texto) <= 1:
        return True
    
    if texto[0] != texto[-1]:
        return False
    
    return es_palindromo(texto[1:-1])
print("="*50)
print("PRUEBAS PALÍNDROMO")
print(es_palindromo("anita"))          # True
print(es_palindromo("reacear"))        # True
print(es_palindromo("python"))         # False
print(es_palindromo("A man a plan"))   # True




def es_palindromo_for(texto):
    texto = texto.replace(" ", "").lower()
    
    for i in range(len(texto)//2):
        if texto[i] != texto[-(i+1)]:
            return False
    return True

print("="*50)
print("PALÍNDROMO - FOR")
print(es_palindromo_for("anita"))
print(es_palindromo_for("python"))



def es_palindromo_while(texto):
    texto = texto.replace(" ", "").lower()
    
    i = 0
    j = len(texto) - 1
    
    while i < j:
        if texto[i] != texto[j]:
            return False
        i += 1
        j -= 1
    
    return True

print("="*50)
print("PALÍNDROMO - WHILE")
print(es_palindromo_while("anita"))
print(es_palindromo_while("python"))



def hanoi(n, origen, destino, auxiliar):
    if n == 0:
        return
    
    hanoi(n-1, origen, auxiliar, destino)
    print(f"Mover disco {n} de {origen} a {destino}")
    hanoi(n-1, auxiliar, destino, origen)

    print("="*50)
print("PRUEBAS TORRES DE HANOI (n=3)")
hanoi(3, "A", "C", "B")
print("="*50)



def movimientos_hanoi_for(n):
    movimientos = 0
    for i in range(1, n+1):
        movimientos = 2**i - 1
    return movimientos

print("="*50)
print("HANOI - FOR")
print(movimientos_hanoi_for(3))
print(movimientos_hanoi_for(4))



def movimientos_hanoi_while(n):
    i = 1
    movimientos = 0
    
    while i <= n:
        movimientos = 2**i - 1
        i += 1
    
    return movimientos

print("="*50)
print("HANOI - WHILE")
print(movimientos_hanoi_while(3))
print(movimientos_hanoi_while(4))



def multiplicar(a,b):
    if b == 0:
        return 0
    
    # Caso recursivo
    return a + multiplicar(a, b -1)
print("="*50)
print(multiplicar(4,4))
print(multiplicar(6,5))
print(multiplicar(8,3))



#for
def multiplicar(a,b):
    
    if b == 0:
        return 0
    resultado = 0

    for i in range(b):
        resultado += a # suma repetida

    return resultado
print("="*50)
print(multiplicar(4,4))
print(multiplicar(6,5))
print(multiplicar(8,3))


#whiel
def multiplicar(a,b):

    if b == 0:
        return 0
    resultado = 0
    contador = 0

    while contador < b:
        resultado += a
        contador += 1

    return resultado 
print("="*50)
print(multiplicar(4,4))
print(multiplicar(6,5))
print(multiplicar(8,3))

