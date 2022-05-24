import random
import time # para agregar tiempo 

# definir 
def ambiente():
    global estado 
    estado = [] 
    for i in range (3): # Rango 3 puesto que son tres entorno
        ambientes = random.randint (0,2) # el rango osilan entre 0 a 2 ya que hay estarian los tres entornos
        estado.append(ambientes) 
        print (estado) #imprimir mi estado actual
        
        def agente(): #Inicializo la funcion
            for x in range (3):
                ambiente ()
        
        #ENTORNO DEL LAS AULAS
        #Estados: Alerta 0, Encendido 1, Apagado 2.
        if estado [0] == 1: 
            print ('En Alerta Aula.') 
            print ('Alertando...')
            time. sleep (5) #Hace un esfuerzo ya que cambio de estado
            print('Ambiente Natural en la Aula \n')  #imprime el estado actual del sensor de humo
        elif estado [1] == 1:
            print ('Ambiente Normal en la Aula.')
            print ('Ambiente Natural en la Aula \n') 
            #Aqui no hace ningun esfuerzo ya que su estado se mantiene
        if estado [2]== 1:
            print ('Agente Apagado, en la Aula.') 
            print ('Encendido el agente en la Aula...') 
            time.sleep(5) #Hace un esfuerzo por esto se agrega un timepo
            print('Listo para trabajar en la Aula\n')
            #Entorno del Laboratorio
        elif estado [0] == 1: # lab es igual a una alerta y debe pasar a encendido
            print ('En Alerta el Laboratorio.') # imprimir el estado
            print ('Alertando...') 
            time. sleep (5) # generando costo aumenta el tiempo 
            print('Ambiente Natural en el Laboratorio \n') 
        if estado [1] == 1:
            print ('Ambiente Normal en el Laboratorio.') 
            print ('Ambiente Natural en el Laboratorio \n') 
	    # No genera costo por lo tanto no hace suma a ningun tiempo 
        if estado [2]== 1: 
            print ('Agente Apagado, en el Laboratorio.') 
            print ('Encendido el agente en el Laboratorio...') 
            time.sleep(5) #genera un costo
            print('Listo para trabajar en el Laboratorio \n')