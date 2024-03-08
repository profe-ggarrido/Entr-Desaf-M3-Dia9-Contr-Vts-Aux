'''
PROCESOS PREVIOS: PARA EL DESARROLLO PRIMERO HICE LA SIGUIENTE LISTA EN ELBLOC:
1.- inicio
2.- leer paciente
3.- realizar estimulo
4.- ¿responde a estimulo?
5.- en caso de SI "llevarlo a hostipal" y Fin proceso
6.- En  caso de NO abrir la via aerea
7.- ¿al abrir via respira?
8.- en caso de si posicionar para mejor ventilacion y fin proceso
9.-en caso de no administrar 5 ventilaciones y llamar ambulancia
10.- ¿presenta signos de vida?
11.- en caso de no, preguntar si llego ambulancia y fin proceso
12.- seguir y volver a preguntar si tiene signos de vida entonces "reevaluar a la espera de la ambulancia" y preguntar si "llegò la ambulancia y fin
13.- en caso contrario "administrar compresiones2 y fin del proceso

Todo segùn el diagra de flujo presentado en el material del LMS

'''

# Paso 1: Inicio
print("Inicio del proceso")

# Paso 2: Leer paciente
print("Paciente leído")

# Paso 3: Realizar estímulo
print("Estímulo realizado")


respuesta = input("¿Responde al estímulo? (SI/NO): ").upper()

if respuesta == "SI":
    print("Llevar al paciente al hospital")
    print("Fin del proceso")
    
elif respuesta == "NO":
    print("Abrir la vía aérea")
    respira = input("¿Al abrir la vía aérea respira? (SI/NO): ").upper()
    
    if respira == "SI":
        print("Posicionar al paciente para mejor/suficiente ventilación")
        print("Fin del proceso")
        
    elif respira == "NO":
        print("Administrar 5 ventilacione y Llamar a la ambulancia")
        
        signos_vida = input("¿Presenta signos de vida? (SI/NO): ").upper()
        
        if signos_vida == "SI":
            print("Reevaluar al paciente a la espera de la ambulancia")
            llegada_ambulancia = input("¿Ha llegado la ambulancia? (SI/NO): ").upper()
            
            while llegada_ambulancia != "SI":  # Ciclo basado en la llegada de la ambulancia
                print("Esperando la llegada de la ambulancia...")
                llegada_ambulancia = input("¿Ha llegado la ambulancia? (SI/NO): ").upper()
                
            print("Fin del proceso")
            
        elif signos_vida == "NO":
            print("Administrar compresiones y fin del proceso")
            llegada_ambulancia = input("¿Ha llegado la ambulancia? (SI/NO): ").upper()
            
            while llegada_ambulancia != "SI":  # Ciclo basado en la llegada de la ambulancia
                print("Esperando la llegada de la ambulancia...")
                llegada_ambulancia = input("¿Ha llegado la ambulancia? (SI/NO): ").upper()
                
            print("Fin del proceso... CHAO PESCAO..")

