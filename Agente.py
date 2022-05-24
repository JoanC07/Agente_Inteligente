#Informacion del Agente
# gente: Diagnóstico de pantalla, batería y disco duro de laptops
#Estados [0 = Buen estado, 1 = Mal estado]
#Ubicaciones: D = Disco, B = Bateria y P = Pantalla 
#Si el usuario desea ingresar por teclado debe ser de esta estructura "D" debe ser mayuscula.

def diagnostico():
    objetivo = {'D': '0', 'B': '0', 'P': '0'} #Objetivo de nuestro agente 
    costo = 0 # Costo se inicia en 0

    ubicacion_laptop = input("Ingrese la ubicacion para el diagnostico: ") #Ubicacion para el diagnostico
    ingreso_estado = input("Ingrese el estado del: " +ubicacion_laptop+ " ") #Si se encuentra en 0/1

    if (ubicacion_laptop  == 'D'):
        ubicacion2_estado = input("Ingrese el estado de B") # Se indica si esta de estado 0/1 en dicha ubicacion.
        ubicacion3_estado = input("Ingrese el estado de P") # Se indica si esta de estado 0/1 en dicha ubicacion.
        print("Objetivo:" + str(objetivo)) #Los objetivos esperados por el agente
        print("La ubicacion para nuestro diagnostico se encuentra en B")# Ubicacion del diagnostico
