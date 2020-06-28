import random

def checkLimits(x, y, tamano):
	if x < tamano and y < tamano and x >=0 and y >= 0:
		return True
	return False 
	

def checkBomba(x, y, listaBombas):
	if [x, y] in listaBombas:
		return True
	return False

def debugCampoBombas(campo, tamano):
	for x in range(tamano):
		for y in range(tamano):
			if campo[x][y] >= 0:
				print(campo[x][y], end="")
			else:
				print("B", end='')
			
		print()
	print()

def createCampo(tamano, bombas):
	campoBombas = []
	campoUsuario = []

	#Inicializar
	for i in range(tamano):
		campoUsuario.append(list())
		campoBombas.append(list())
		for j in range(tamano):
			campoUsuario[i].append("-")
			campoBombas[i].append(0)

	debugCampoBombas(campoBombas, tamano);

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

	debugCampoBombas(campoBombas, tamano);

print(createCampo(30,100))

