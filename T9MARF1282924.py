print("Ejercicio 1: Conversión de unidades de longitud")

def metros_a_sistema_ingles(cantidad_metros):
    millas = cantidad_metros / 1609.34
    kilometros = cantidad_metros / 1000
    pies = cantidad_metros * 3.28084
    pulgadas = pies * 12
    yardas = pies / 3
    return millas, kilometros, pies, pulgadas, yardas

nombre_usuario = input("Ingrese su nombre: ")
codigo_estudiante = input("Ingrese su código de estudiante: ")
print(f"{nombre_usuario} - {codigo_estudiante}")

while True:
    cantidad_metros = float(input("Ingrese una cantidad en metros: "))
    millas, kilometros, pies, pulgadas, yardas = metros_a_sistema_ingles(cantidad_metros)

    print("Resultado:")
    print(f"Millas: {millas:.2f}")
    print(f"Kilómetros: {kilometros:.2f}")
    print(f"Pies: {pies:.2f}")
    print(f"Pulgadas: {pulgadas:.2f}")
    print(f"Yardas: {yardas:.2f}")

    continuar = input("¿Desea ingresar otra cantidad en metros? (si/no): ")
    if continuar.lower() != 'si':
        break

print("Operaciones realizadas correctamente")
