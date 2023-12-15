import os
isActive = True
rta = ""

menu = "1. sumar\n2 . Restar\n0.salir"
while (isActive):
    try:
        rta = int(input(menu))
    except ValueError:
        print("Error en el dato")
    else:
        if(rta == 1):
            print ("sumando")
        elif (rta == 2):
            print ("Restando")
        elif ("rta == 0"):
            print ("Ok chao")
            os.system("pause")
        else:
            print ("La opcion que ingreso es invalida..")
            os.system ("pause")

    
#while (isActive):
#   os. system ("cls")
#    rta = input("Desea continuar con la ejecucion S(si) o Enter (No)").upper()
#   while (rta is not "S"):
#        print("Ha ingresado una opcion invalida")
#        os. system("pause")
#        os. system("cls")
#       rta = input ("Desea continuar con la ejeccion S(si) o Enter (No)").upper()
#    if (bool(rta) == False):
#      isActive = bool(rta)