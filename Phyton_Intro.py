sum = 1+2
print(sum)

sum = 1 + 2 # 3
product = sum * 2
print(product)

# Declaramos la variable
distancia_a_alfa_centauri = 4.367

# Descubrimos su tipo de datoprint
print(type(distancia_a_alfa_centauri))

#Operadores
left_side = 10
right_side = 5
print(left_side / right_side) # 2

#Fechas
# Importamos la biblioteca 
from datetime import date

# Obtenemos la fecha de hoy
date.today()

# Mostramos la fecha en la consola
print(date.today())

#print("Today's date is: " + date.today()) # With Error
print("Today's date is: " + str(date.today()))

print("Bienvenido al programa de bienvenida")
name = input("Introduzca su nombre ")
print("Saludos: " + name)

print("Calculadora")
first_number = input("Primer número: ")
second_number = input("Segundo número: ")
print(first_number + second_number)
print(int(first_number) + int(second_number))