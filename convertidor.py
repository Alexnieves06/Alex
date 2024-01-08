"""Convertidor de unidades"""

#Definicion de funciones
def metros_a_kilometros(metros):
    return metros / 1000

def kilometros_a_metros(kilometros):
    return kilometros * 1000

def centimetros_a_metros(centimetros):
    return centimetros / 100

def metros_a_centimetros(metros):
    return metros * 100

def pulgadas_a_milesimas(pulgadas):
    return pulgadas * 1000

def milesimas_a_pulgadas(milesimas):
    return milesimas / 1000

#bucle para interaccion con el usuario
while True:    
    print("""
          
        ¡Bienvenido al convertidor de unidades! Por favor elige una opcion.
          
        Ingrese:
          
        Para convertir de metros a kilometros ingrese : 1 
        Para convertir de kilometros a metros ingrese : 2 
        Para convertir centimetros a metros ingrese   : 3
        Para convertir de metros a centimetros ingrese: 4
        Para convertir de pulgadas a milesimas ingrese: 5
        Para convertir de milesimas a pulgadas ingrese: 6
        Para salir ingrese: 0
        """)

    opcion = int(input("Ingrese su opcion: "))

    if opcion == 0:
        print("Saliendo del programa... ¡Hasta luego!")
        break

    elif opcion in [1, 2, 3, 4, 5, 6]:
        if opcion == 1:
            print("Convertir de metros a kilómetros.")
            longitud = float(input("Ingrese la longitud en metros: "))
            resultado = metros_a_kilometros(longitud)
            print(f"{longitud} metros son {resultado} kilómetros.")

        elif opcion == 2:
            print("Convertir de kilómetros a metros.")
            longitud = float(input("Ingrese la longitud en kilómetros: "))
            resultado = kilometros_a_metros(longitud)
            print(f"{longitud} kilómetros son {resultado} metros.")

        elif opcion == 3:
            print("Convertir centímetros a metros.")
            longitud = float(input("Ingrese la longitud en centímetros: "))
            resultado = centimetros_a_metros(longitud)
            print(f"{longitud} centímetros son {resultado} metros.")

        elif opcion == 4:
            print("Convertir de metros a centímetros.")
            longitud = float(input("Ingrese la longitud en metros: "))
            resultado = metros_a_centimetros(longitud)
            print(f"{longitud} metros son {resultado} centímetros.")

        elif opcion == 5:
            print("Convertir de pulgadas a milesimas.")
            longitud = float(input("Ingrese la longitud en pulgadas: "))
            resultado = pulgadas_a_milesimas(longitud)
            print(f"{longitud} pulgadas son {resultado} milesimas.")

        elif opcion == 6:
            print("Convertir de milesimas a pulgadas.")
            longitud = float(input("Ingrese la longitud en milesimas: "))
            resultado = milesimas_a_pulgadas(longitud)
            print(f"{longitud} milesimas son {resultado} pulgadas.")

    else:
        print("Opción no válida, favor ingresar 1, 2, 3, 5, 6 o 0.")
