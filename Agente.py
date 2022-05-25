#Informacion del Agente
# gente: Diagnóstico de pantalla, batería y disco duro de laptops
#Estados [0 = Buen estado, 1 = Mal estado]
#Ubicaciones: D = Disco, B = Bateria y P = Pantalla 
#Si el usuario desea ingresar por teclado debe ser de esta estructura "D" debe ser mayuscula.

def diagnostico():
    objetivo = {'D': '0', 'B': '0', 'P': '0'} #Objetivo de nuestro agente 
    costo = 0 # Costo se inicia en 0

    ubicacion_laptop = input("Ingrese la ubicacion para el diagnostico: ") #Ubicacion para el diagnostico
    estado = input("Ingrese el estado del: " +ubicacion_laptop+ " ") #Si se encuentra en 0/1

    if (ubicacion_laptop  == 'D'):
        ubicacion2_estado = input("Ingrese el estado de B") # Se indica si esta de estado 0/1 en dicha ubicacion.
        ubicacion3_estado = input("Ingrese el estado de P") # Se indica si esta de estado 0/1 en dicha ubicacion.
        print("Objetivo:" + str(objetivo)) #Los objetivos esperados por el agente
        print("La ubicacion del diagnostico se encuentra en D")# Ubicacion del diagnostico
        
        if(estado == '1'): #El dignostico del disco (D) esta en mal estado
            print("El diagnostico reporta un mal estado")
            objetivo['D'] ='0' #Diagnostico pasara a 0
            costo += 1 #Aumenta el costo
            print("El diagnostico reporta buen estado en el D")
            print("El costo actual es: " +str(costo)) 
                
            if(ubicacion2_estado == '1'):
                print("El diagnostico de B")
                print("El diagnostico empezara ahora en B") 
                costo += 1 #Cada vez que el diagnostico este en buen estado aumentara
                print("El costo actual es: " +str(costo)) #Costo actual
                objetivo['B'] ='0' #Diagnostico dara buen estado
                costo += 1 #Cada vez que el diagnostico este en buen estado aumentara
                print("El diagnostico muestra en buen estado en B")
                print("El costo actual es: "  +str(costo)) #Muestra el costo actual 