import random

def checkLimits(x, y, tamano):
	if x < tamano and y < tamano and x >=0 and y >= 0:
		return True
	return False 
	

def checkBomba(x, y, bombas):
	if [x, y] in bombas:
		return True
	return False



def debugCampoBombas(campo, tamano):
	for x in range(tamano):
		for y in range(tamano):
			if int(campo[x][y]) >= 0:
				print(campo[x][y], end="")
			else:
				print("B", end='')
			
		print()
	print()

def showBombas(bombas):
	campo = []
	i = 0
	for fila in bombas:
		campo.append(list())
		for celda in fila:
			if celda == -1: 
				campo[i].append("B")
			elif celda == 0:
				campo[i].append("0")
			else:
				campo[i].append(str(celda))
				
		i += 1

	return campo

def selectCelda(x, y, bombas, campoUsuario, tamano):
	if bombas[x][y] == -1:
		return showBombas(bombas), False;

	adyancencia = [[-1,-1],[-1, 0],[-1, 1],[ 0,-1],
				   [ 0, 1],[ 1,-1],[ 1, 0],[ 1, 1]]

	queue = []
	queue.append((x,y))

	while queue:
		celda = queue.pop(0);
		x1 = celda[0]
		y1 = celda[1]

		if(campoUsuario[x1][y1] != "-"):
			continue;

		if bombas[x1][y1] > 0 :
			campoUsuario[x1][y1] = str(bombas[x1][y1])
		else:
			campoUsuario[x1][y1] = "0";

			for a, b in adyancencia:
				x2 = x1 + a
				y2 = y1 + b
				if checkLimits(x2, y2, tamano) and bombas[x2][y2] != -1 and campoUsuario[x2][y2] == "-":
					queue.append((x2,y2))

	return campoUsuario, True;

			
def createCampo(tamano, bombas):
	campoUsuario = []
	campoBombas = []
	#Inicializar
	for i in range(tamano):
		campoUsuario.append(list())
		campoBombas.append(list())
		for j in range(tamano):
			campoUsuario[i].append("-")
			campoBombas[i].append(0)

	#Poner bombas
	posPosibles = []
	for i in range(tamano):
		for j in range(tamano):
			punto = [i,j]
			posPosibles.append(punto)

	listaBombas = random.sample(posPosibles, bombas)
	listaBombas.sort()

	adyancencia = [[-1,-1],[-1, 0],[-1, 1],[ 0,-1],
				   [ 0, 1],[ 1,-1],[ 1, 0],[ 1, 1]]

	for i, j in listaBombas:
		campoBombas[i][j] = -1 
		for x, y in adyancencia:
			a = i+x
			b = j+y
			if checkLimits(i+x, j+y, tamano) and not(checkBomba(i+x, j+y, listaBombas)):
				campoBombas[i+x][j+y] += 1

	out = [campoUsuario, campoBombas]
	return out;
