numeroSecreto = 777

print(
"""
+==================================+
| Bienvenido a mi juego, muggle!   |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

numero = int(input("Ingresa un numero: "))

while numero != numeroSecreto:
    print("¡Ja, ja! ¡Estás atrapado en mi ciclo!")
    numero = int(input("Ingresa un numero: "))

print("¡Bien hecho, muggle! Eres libre ahora")
