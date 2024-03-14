print("Herramienta Conversión de unidades de longitud")
#Valores para conversiones
def metros_a_sistema_ingles(cantidad_metros):
    millas = cantidad_metros / 1609.34
    kilometros = cantidad_metros / 1000
    pies = cantidad_metros * 3.28084
    pulgadas = pies * 12
    yardas = pies / 3
    return millas, kilometros, pies, pulgadas, yardas

nombre = input("Ingrese su nombre: ")
codigo = input("Ingrese su código de estudiante: ")
print(f"{nombre} - {codigo}")

cantidad_metros = float(input("Ingrese una cantidad en metros: "))
millas, kilometros, pies, pulgadas, yardas = metros_a_sistema_ingles(cantidad_metros)

print("Resultado:")
print(f"Millas: {millas: .2f}")
print(f"Kilómetros: {kilometros: .2f}")
print(f"Pies: {pies: .2f}")
print(f"Pulgadas: {pulgadas: .2f}")
print(f"Yardas: {yardas: .2f}")

print("Operaciones realizadas correctamente, ¡Espero haberte ayudado!")