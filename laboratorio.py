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