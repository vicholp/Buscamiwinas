import os
import buscaminas
os.system('color')


#Esto tiene que ser un dict
colores = [('0','\033[0;37;48m'),           #Negro
           ('-','\033[0;37;47m'),           #Blanco
           ('B','\033[0;37;41m'),           #Rojo
           ('F','\033[0;37;43m'),           #Amarillo
           ('num','\033[0;37;44m'),         #Azul
           ('X','\033[0;37;42m'),           #Verde
           ('-','\033[0;37;45m'),           #Magenta
           ('celeste','\033[0;37;46m')]

nativo='\033[m'


def copiarLienzo(lienzo):

    copia = []
    for b in lienzo:
        copia.append(list(b))
    return copia

def asignarColor(colores, celda):
    for simbolo,codigo in colores:
        if celda.isalnum() and simbolo == "num":
            return codigo + celda + nativo
        if simbolo == celda:
            return codigo + ' ' + nativo
        

def printCampo(campo, tamano):

    #Print numero de columnas
    print("  ", end='')
    for i in range(1, tamano+1):
        print(i//10, end='')

    print()
    print("  ", end='')
    for i in range(1, tamano+1):
        print(i%10, end='')
    print()

    #Print tablero
    n_fila = 1
    for fila in campo:
        if n_fila < 10:
            out = '0' + str(n_fila)
        else:
            out = str(n_fila)
        for celda in fila:
            out += asignarColor(colores,celda)

        print(out)

        out = ''
        n_fila += 1
    
def menuJugar():
    print("Opciones:")
    print("1- Marcar celda")
    print("2- Poner banderita")
    print("3- Rendirse")

    opcion = int(input("Seleccione una opción: "))
    return opcion

def menuConfirmar():
    return True
    
def menuInputInvalido():
    print("Opcion invalida, vuelve a intentarlo.")

def validarInput(i, min, max):

    if(i >= min and i < max):
        return True
    return False

def seleccionarCasilla(tamano):
    fila = int(input("Ingrese fila: "))-1
    columna = int(input("Ingrese columna: "))-1

    while not(buscaminas.checkLimits(fila, columna, tamano)):
        print("Opción inválida, intente de nuevo")
        fila = int(input("Ingrese fila: "))-1
        columna = int(input("Ingrese columna: "))-1

    return fila, columna

def seguirJugando():
    elegir = ''
    while elegir != 'si' and elegir != 'no':
        elegir = input("¿Te gustaría jugar de nuevo?(si/no): ")
    if elegir == 'si':
        return True
    return False

def endGame(estado):
    if estado == 'Derrota':
        print("Lo siento, perdiste")
    else:
        print("Felicitaciones, ganaste!")
    continuar = seguirJugando()
    return continuar


    