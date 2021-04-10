"""Guarde en lista `naturales` los primeros 100 números naturales (desde el 1) 
usando el bucle while
"""
S = 1
naturales = []
while S < 101:
    naturales.append(S)
    S += 1

print("\n\tLos primeros 100 números naturales desde 1 ==>  ",naturales)


"""Guarde en `acumulado` una lista con el siguiente patrón:

['1','1 2','1 2 3','1 2 3 4','1 2 3 4 5',...,'...47 48 49 50']

Hasta el número 50.
"""
accumulated = []

for S in range(2, 52):
  cadena=''
  for P in range(1, S):
    cadena =  cadena + ' ' + str(P)
  accumulated.append(cadena[1:])

print("\t\nAcumulado de una lista con el siguiente patrón  '1', '1 2', '1 2 3', '1 2 3 4', '1 2 3 4 5', '1 2 3 4 5 6'   Hasta [50]  : \n",accumulated) 


"""Guarde en `suma100` el entero de la suma de todos los números entre 1 y 100:
"""

suma100 = 0
for S in naturales:
  suma100 = S +suma100

print("\nLa suma Total de todos los números entre 1 y 100 es : " ,suma100)


"""Guarde en `tabla100` un string con los primeros 10 múltiplos del número 134, 
separados por coma, así:

'134,268,...'

"""
table100 = ''
for i in range(1, 11):
 table100 = table100 + ',' + str( i * 134)
table100 = str(table100[1:])
print("\n\tLos 10 Primeros Multiplos de 134\n\t" ,table100)


"""Guardar en `multiplos3` la cantidad de números que son múltiplos de 3 y 
menores a 300 en la lista `lista1` que se define a continuación (la lista 
está ordenada).
"""
lista1 = [12, 15, 20, 27, 32, 39, 42, 48, 55, 66, 75, 82, 89, 91, 93, 105, 123, 132, 150, 180, 201, 203, 231, 250, 260, 267, 300, 304, 310, 312, 321, 326]

Base = [S for S in lista1  if S % 3 == 0 and S < 300]
multiples3 = len(Base)

print("\n\tCantidad de números que son múltiplos de 3 y  menores a 300",multiples3)
 
"""Guardar en `regresivo50` una lista con la cuenta regresiva desde el número 
50 hasta el 1, así:

[
  '50 49 48 47...',
  '49 48 47 46...',
  ...
  '5 4 3 2 1',
  '4 3 2 1',
  '3 2 1',
  '2 1',
  '1'
]
"""

regressive = []

for S in range(50, 0, -1):
  cadena=''
  for P in range(S, 0, -1):
    cadena =  cadena + ' ' + str(P)
  regressive.append(cadena[1:])

print("\n\tLista de cuenta regresiva desde el número 50 hasta el 1",regressive)


"""Invierta la siguiente lista usando el bucle for y guarde el resultado en 
`invertido` (sin hacer uso de la función `reversed` ni del método `reverse`)
"""
lista2 = list(range(1, 70, 5))

invested = []
for a in range(71, 0, -5):
  invested.append(a)
invested = invested[1:]
print(invested)


"""Guardar en `primos` una lista con todos los números primos desde el 37 al 300

Nota: Un número primo es un número entero que no se puede calcular multiplicando 
otros números enteros.
"""

cousins = []
Inicio = 37

while Inicio <= 300:
  cont =1
  x = 0
  while cont <= Inicio:
    if Inicio % cont ==0:
      x = x+1
    cont = cont + 1
  if x == 2:
    cousins.append(Inicio)
  Inicio = Inicio + 1

print("\n\tLista de todos los números primos desde el 37 al 300 ",cousins)

"""Guardar en `fibonacci` una lista con los primeros 60 términos de la serie de 
Fibonacci.
Nota: En la serie de Fibonacci, los 2 primeros términos son 0 y 1, y a partir 
del segundo cada uno se calcula sumando los dos anteriores términos de la serie.

[0, 1, 1, 2, 3, 5, 8, ...]

"""
fibonacci= [0,1]

for i in range(2, 60):
  fibonacci.append(fibonacci[-1] + fibonacci[-2])

print("\n\tLista con los primeros 60 términos de la secuencia de Fibonacci ",fibonacci)


"""Guardar en `factorial` el factorial de 30
El factorial (símbolo:!) Significa multiplicar todos los números enteros desde
el 1 hasta el número elegido.

Por ejemplo, el factorial de 5 se calcula así:

5! = 5 × 4 × 3 × 2 × 1 = 120
"""

factorial = 1
for i in range(1, 31):
  factorial = factorial * i
print("\n\tel factorial de Numero [ 30 ] = ",factorial)


"""Guarde en lista `pares` los elementos de la siguiente lista que esten 
presentes en posiciones pares, pero solo hasta la posición 80.
"""

lista3 = [941, 149, 672, 208, 99, 562, 749, 947, 251, 750, 889, 596, 836, 742, 512, 19, 674, 142, 272, 773, 859, 598, 898, 930, 119, 107, 798, 447, 348, 402, 33, 678, 460, 144, 168, 290, 929, 254, 233, 563, 48, 249, 890, 871, 484, 265, 831, 694, 366, 499, 271, 123, 870, 986, 449, 894, 347, 346, 519, 969, 242, 57, 985, 250, 490, 93, 999, 373, 355, 466, 416, 937, 214, 707, 834, 126, 698, 268, 217, 406, 334, 285, 429, 130, 393, 396, 936, 572, 688, 765, 404, 970, 159, 98, 545, 412, 629, 361, 70, 602]



pairs = []

for S in range(0, 81):
  if S % 2 == 0:
    pairs.append(lista3[S])

print("\n\tlista que esten presentes en posiciones pares, pero solo hasta la posición 80",pairs)


"""Guarde en lista `cubos` el cubo (potencia elevada a la 3) de los números del  1 al 100. 
"""

cubes = []

for S in range(1, 101):
  cubes.append(S ** 3)
print("\n\tel cubo (potencia elevada a la 3) de los números del  1 al 100",cubes)


"""Encuentre la suma de la serie 2 +22 + 222 + 2222 + .. hasta sumar 10 términos  y guardar resultado en variable `suma_2s` 
"""
Inicio = 0

for S in range(0, 11):
    P = 10 ** S * (10 - S) * 2
    Inicio = P + Inicio
suma_2s = Inicio

print("\n\tSuma de la serie 2 + 22 + 222 + 2222 + .. hasta sumar 10 términos = ",suma_2s)


"""Guardar en un string llamado `patron` el siguiente patrón llegando a una cantidad máxima de asteriscos de 30. 
*
**
***
****
*****
******
*******
********
*********
********
*******
******
*****
****
***
**
*
"""

A = '*\n'
B = '******************************\n'
C = '*'
for S in range(2, 30):
  C = '*'
  C = C * S
  A = A + C + '\n'

print(A)

for S in range(29, 0, -1):
  C = '*'
  C = C * S
  B = B + C + '\n'
print(B)

pattern = A + B
pattern = pattern[:-1]
print("\n\tpatrón llegando a una cantidad máxima de asteriscos de 30 ", pattern)


End = '100%'
print("Casi Que No ....!!!!: \"¿Acabo?\"")
print('En Verdad Termine: \'¡ Por Fin !\'')
print("\n\tTerminamos" ,End)
