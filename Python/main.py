import vista
import buscaminas

#Todas tienen una relacion 0.16
dificultades = 	{
					'facil': [8, 10],
					'normal': [15, 40], 
					'dificil': [30, 150]
				}

dificultad = "facil" #DEBUG

while dificultad not in dificultades:
    dificultad = input("Seleccione dificultad(facil/normal/dificil): ")

size_campo = dificultades[dificultad][0]
n_bombas = dificultades[dificultad][1]

#campo, campoBombas = buscaminas.createCampo(size_campo, n_bombas);

continuar = True #para seguir jugando después de la derrota
estado = True #Jugando:True, Derrota, Victoria.

while continuar:
	campo, campoBombas = buscaminas.createCampo(size_campo, n_bombas);
	vista.printCampo(campo, size_campo);
	opcion = vista.menuJugar();

	if opcion == 1:
		x, y = vista.seleccionarCasilla(size_campo);

		#Esto tiene que ser una funcion
		t = campo[x][y]
		campo[x][y] = "X";
		vista.printCampo(campo, size_campo);
		campo[x][y] = t

		o = int(input("Sure? 1/0 "))
		if(o == 1):
			campo, estado = buscaminas.selectCelda(x, y, campoBombas, campo, size_campo);
				
		vista.printCampo(campo, size_campo);
		while(estado == True):
			x, y = vista.seleccionarCasilla(size_campo);

			#Esto tiene que ser una funcion
			t = campo[x][y]
			campo[x][y] = "X";
			vista.printCampo(campo, size_campo);
			campo[x][y] = t

			o = int(input("Sure? 1/0 "))
			if(o == 1):
				campo, estado = buscaminas.selectCelda(x, y, campoBombas, campo, size_campo);
				
				
			vista.printCampo(campo, size_campo);
		
		if not estado:
			continuar = vista.endGame('Derrota')


	#Me tiene que dejar jugar denuevo





