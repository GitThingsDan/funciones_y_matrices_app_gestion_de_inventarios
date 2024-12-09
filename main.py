from dal.db_marcas import agregar_marca, mostrar_marcas
from dal.db_modelos import agregar_modelo, mostrar_modelos, eliminar_modelo
from dal.db_tipo_cal import mostrar_tipo_calzado
from colorama import Fore
import os
opcion =""


while opcion != '0': 
                os.system('cls')
                print("\nSistema de Gestión de inventario") 
                print(Fore.BLUE + "[1] Añadir Marca") 
                print(Fore.BLUE + "[2] Ver Marcas") 
                print(Fore.GREEN + "[3] Añadir Modelos") 
                print(Fore.GREEN + "[4] Ver Modelos") 
                print(Fore.GREEN + "[5] Eliminar Modelos")
                print(Fore.CYAN + "[6] Ver tipos de calzado")
                print(Fore.LIGHTMAGENTA_EX + "[0] salir")

                opcion = input(Fore.LIGHTWHITE_EX + "Elegir una opcion: ") 

                if opcion == "1": 
                    agregar_marca()
                elif opcion == "2":
                    mostrar_marcas()
                elif opcion == "3":
                    agregar_modelo()
                elif opcion == "4":
                    mostrar_modelos()
                elif opcion =="5":
                    eliminar_modelo()
                elif opcion == "6":
                    mostrar_tipo_calzado()
                elif opcion == "0":  
                    print("Hasta luego.")
                else:
                    print(f"{opcion} no es una opción válida")
                os.system('pause')

