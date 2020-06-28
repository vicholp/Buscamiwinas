import vista
import buscaminas


dificultades = 	{
					'facil': [8, 8],
					'normal': [15, 40], 
					'dificil': [30, 100]
				}

dificultad = "dificil" #DEBUG

while dificultad not in dificultades:
    dificultad = input("Seleccione dificultad(facil/normal/dificil): ")

size_campo = dificultades[dificultad][0]
n_bombas = dificultades[dificultad][1]

campo = buscaminas.createCampo(size_campo, n_bombas);

vista.printCampo(campo,size_campo)

estado = True #Jugando:True, Derrota, Victoria.

while(estado):
	jugada = vista.menuJugar()

	estado = "Perdi"
	

