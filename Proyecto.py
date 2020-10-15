#Base de conocimiento Proyecto final programacion III
# encoding: utf-8
from pyDatalog import pyDatalog


#Terminos

pyDatalog.create_terms('sintomas_en_enfermedades, sintomas_en_plagas, condicion_en_enfermedades, condicion_en_plagas, manejo_enfermedades,dano_de_las_enfermedades, dano_de_las_plagas manejo_de_las_plagas ')
pyDatalog.create_terms('X,Y,Z')


#sintomas_en_enfermedades

+ sintomas_en_enfermedades('Pudricion de raices', 'deformacion')
+ sintomas_en_enfermedades('Pudricion de raices', 'deformacion de la raiz')
+ sintomas_en_enfermedades('Pudricion de raices', 'cancros rojizos y hundidos')
+ sintomas_en_enfermedades('Pudricion de raices', 'pequeños puntos rojizos alargados')
+ sintomas_en_enfermedades('amarillamiento', 'color cafe rojizo')
+ sintomas_en_enfermedades('amarillamiento', 'tejido interno color cafe o rojizo oscuro')
+ sintomas_en_enfermedades('amarillamiento', 'felpa color anaranjado claro')
+ sintomas_en_enfermedades('mal de esclerocio', 'masa de color blanco')
+ sintomas_en_enfermedades('mal de esclerocio', 'marchitez repentina en plantas')
+ sintomas_en_enfermedades('mal de esclerocio', 'lesiones oscuras')
+ sintomas_en_enfermedades('mancha angular', 'manchas color gris o cafe')
+ sintomas_en_enfermedades('mancha angular', 'caida de las hojas inferiores')
+ sintomas_en_enfermedades('mancha angular', 'vainas con manchas cafes o rojizas')
+ sintomas_en_enfermedades('nematodos falsa mancha angular', 'puntos amarillentos')                                                                                           
+ sintomas_en_enfermedades('nematodos falsa mancha angular', 'manchas oscuras')                                                                                               
+ sintomas_en_enfermedades('nematodos falsa mancha angular', 'las vainas no presentan brotes')                                                                                 
+ sintomas_en_enfermedades('nematodos falsa mancha angular', 'no tienen bastoncitos debajo de la hoja ')                                                                      
+ sintomas_en_enfermedades('antracnosis', 'manchas redondas y profundas en las vainas')
+ sintomas_en_enfermedades('antracnosis', 'las vainas se tuercen y no producen grano')
+ sintomas_en_enfermedades('antracnosis', 'manchas de 1mm en las plantas mas jovenes ')

#sintomas_en_plagas

+ sintomas_en_plagas('Roya', 'manchas amarillas con centro oscuro')
+ sintomas_en_plagas('Roya', 'amarillamiento y caida de hojas')
+ sintomas_en_plagas('Mildeo polvoso', 'manchas oscuras o manchas color blancuzco')
+ sintomas_en_plagas('Mildeo polvoso', 'deformacion de las vainas')
+ sintomas_en_plagas('Mildeo polvoso', 'aspectos de tela de araña')
+ sintomas_en_plagas('Mosca blanca', 'caida de las hojas')
+ sintomas_en_plagas('Mosca blanca', 'transmite varios tipos de enfermedad')
+ sintomas_en_plagas('Mosca blanca', 'moho oscuro llamado fumagina')
+ sintomas_en_plagas('Mosca blanca', 'se alimenta de la maleza expulsada por la mosca')

#condicion_en_enfermedades

+ condicion_en_enfermedades('Pudricion de raices', 'temperatura humeda entre el 20 y 25%')
+ condicion_en_enfermedades('amarillamiento', 'temperatura humeda y calida entre el 20 y 28%')
+ condicion_en_enfermedades('mal de esclerocio', 'temperatura calida entre el 25 y 35%')
+ condicion_en_enfermedades('mancha angular','temperatura intermedia entre el 18 y 28%')
+ condicion_en_enfermedades('nematodos falsa mancha angular','temperatura moderada entre los 18 y 25%')                                                                 
+ condicion_en_enfermedades('antracnosis',' temperatura fresca entre los 16 y 24%')

#condicion_en_plagas

+ condicion_en_plagas ('roya', 'temperatura moderada entre los 17 y 27%')                                                                                          
+ condicion_en_plagas ('mildeo polvoso', 'temperatura calidos entre los 20 y 25%')                                                                                 
+ condicion_en_plagas ('mosca blanca', 'temperatura calidos entre los 20 y 25%')                                                                                   

#dano_de_las_enfermedades

+ dano_de_las_enfermedades('Pudricion de raices', 'aparecen los daños en alturas de 1500 msnm')
+ dano_de_las_enfermedades('amarillamiento', 'es atacada en la segunda o tercera semana de siembra')
+ dano_de_las_enfermedades('mal de esclerocio', 'es atacada durante todo su ciclo de vida')
+ dano_de_las_enfermedades('mancha angular','bordes angulares en ambos lados de la hoja')
+ dano_de_las_enfermedades('nematodos falsa mancha angular','aparecen varios manchones o remolinos en la planta')                                                   
+ dano_de_las_enfermedades('antracnosis', 'aparecen los daños en alturas de 1500 msnm')

#dano_de_las_plagas

+ dano_de_las_plagas ('roya',' resequedad en la siembra y posterior muerte')
+ dano_de_las_plagas ('mildeo polvoso',' ataca brotes tiernos y flores y cubriendolos asi de un vello blanquecino')
+ dano_de_las_plagas ('mosca blanca',' sustrae la savia de la hoja hasta degradarlas')

#manejo_de_las_enfermedades 

+ manejo_de_las_enfermedades('Pudricion de raices', 'semillas sanas')
+ manejo_de_las_enfermedades('Pudricion de raices', 'rotar con cultivos de maiz y de yuca')
+ manejo_de_las_enfermedades('Pudricion de raices', 'evitar suelos encharcados')
+ manejo_de_las_enfermedades('Pudricion de raices', 'arar a 20 cm de profundidad')
+ manejo_de_las_enfermedades('amarillamiento', 'semilla sana y nueva')
+ manejo_de_las_enfermedades('amarillamiento', 'evitar siembras tupidas y con un mal drenaje')
+ manejo_de_las_enfermedades('amarillamiento', 'rotar con cultivos de maiz, pasto o con sorgo')
+ manejo_de_las_enfermedades('amarillamiento', 'utilizar fungicidas como benomil o carboxin')
+ manejo_de_las_enfermedades('mal de esclerocio', 'semillas sanas y nuevas')
+ manejo_de_las_enfermedades('mal de esclerocio', 'eliminar restos de siembra de 2 a 6 semanas')
+ manejo_de_las_enfermedades('mal de esclerocio', 'productos a base de trichoderma')
+ manejo_de_las_enfermedades('mal de esclerocio', 'utilizar fungicidas como PCNB o carboxin')
+ manejo_de_las_enfermedades('mancha angular','semillas sanas y nuevas')
+ manejo_de_las_enfermedades('mancha angular','eliminar restos de siembras muy afectados')
+ manejo_de_las_enfermedades('mancha angular','rotar por un año con cultivos diferentes al frijol')
+ manejo_de_las_enfermedades('mancha angular','utilizar fungicidas antes de la 5 semana como el benomil o el carbendazim')
+ manejo_de_las_enfermedades('nematodos falsa mancha angular', 'evitar sembrar el frijol despues de cultivo del arroz')
+ manejo_de_las_enfermedades('nematodos falsa mancha angular', 'eliminar malezas y plantas voluntarias al arroz')                                                                                          
+ manejo_de_las_enfermedades('nematodos falsa mancha angular', 'usar cobertura o labranza minima')                                                                                                  
+ manejo_de_las_enfermedades('nematodos falsa mancha angular', 'no sembrar tupidamente para que las hojas sequen de una forma rapida')                                                                      
+ manejo_de_las_enfermedades('antracnosis',' semillas secas y aisladas')
+ manejo_de_las_enfermedades('antracnosis',' eliminar restos de cualquier cosecha y rotar cultivos durante dos años')
+ manejo_de_las_enfermedades('antracnosis','ataques muy tempranos de fungicidas reducen su crecimiento')
+ manejo_de_las_enfermedades('antracnosis','utilizar fungicidas como el benomil o el carboxin')

#manejo_de_las_plagas

+ manejo_de_las_plagas('roya', 'rotar cultivos y eliminar restos de cosechas')
+ manejo_de_las_plagas('roya', 'no se debe sembrar tupidamente')
+ manejo_de_las_plagas('roya', 'utilizar fungicidas como el benomil o el carbendazim')
+ manejo_de_las_plagas('roya', 'aplicar fungicidas despues de la tercera semana o antes de la floracion')
+ manejo_de_las_plagas('mildeo polvoso',' controlando malezas')
+ manejo_de_las_plagas('mildeo polvoso',' quemado del material infectado')
+ manejo_de_las_plagas('mildeo polvoso',' utilizar fungicidas como el zineb o el azufre o el policarbazin')
+ manejo_de_las_plagas('mildeo polvoso',' evitar siembras en lugares donde la temperatura y la humedad sean altas y constantes')
+ manejo_de_las_plagas('mosca blanca', 'rotar cultivos con habichuela o pepino y eliminar restos de cosecha')
+ manejo_de_las_plagas('mosca blanca', 'evitar siembras en lugares donde la temperatura y la humedad sean altas y constantes')
+ manejo_de_las_plagas('mosca blanca', 'evitar cultivos escalonados')
+ manejo_de_las_plagas('mosca blanca', 'evitar cultivos de edades diferentes')
+ manejo_de_las_plagas('mosca blanca', 'evitar todos los residuos de cosechas anteriores')
+ manejo_de_las_plagas('mosca blanca', 'usar insectisidas')

#--------------------------------------------------------------------------------------------------------------------------------#

SintomasFrijol = ['deformacion','deformacion de la raiz']     
def identificacionSintoma(SintomasFrijol):
	print(SintomasFrijol)
	Enfermedadnotoria = {'Pudricion de raices': 0, 'amarillamiento':0, 'mal de esclerocio':0, 'mancha angular':0, 'nematodos(falsa mancha angular)':0, 'antracnosis':0, }
	Enfermedadnotoria = {'Roya':0, 'mildeo polvoso':0, 'mosca blanca':0}
	sintomasLista = []
	print("Posibles sintomas")
	for x in SintomasFrijol:
		print(sintomas(X, x))
		#sintomasLista.append(r)
		for xi in X.data:
			sintomasLista.append(xi)
		for x in sintomasLista:
			if x == 'Pudricion raices':
				Enfermedadnotoria['Pudricion de raices'] = Enfermedadnotoria['Pudricion de raices'] + 1
			elif x == 'amarillamiento':
				Enfermedadnotoria['amarillamiento'] = Enfermedadnotoria['amarillamiento'] + 1
			elif x == 'mal de esclerocio':
				Enfermedadnotoria['mal de esclerocio'] = Enfermedadnotoria['mal de esclerocio'] + 1
			elif x == 'mancha angular':
				Enfermedadnotoria['amarillamiento'] = Enfermedadnotoria['amarillamiento'] + 1
			elif x == 'nematodos(falsa mancha angular)':
				Enfermedadnotoria['nematodos(falsa mancha angular)'] = Enfermedadnotoria['nematodos(falsa mancha angular)'] + 1
			elif x == 'antracnosis':
				Enfermedadnotoria['antracnosis'] = Enfermedadnotoria['antracnosis'] + 1
			elif x == 'Roya':
			    Enfermedadnotoria['Roya'] = Enfermedadnotoria['Roya'] + 1
			elif x == 'Mildeo polvoso':
			    Enfermedadnotoria['Mildeo polvoso'] = Enfermedadnotoria['Mildeo polvoso'] + 1
			elif x == 'mosca blanca':
			    Enfermedadnotoria['mosca blanca'] = Enfermedadnotoria['mosca blanca'] + 1    


		keys = list(Enfermedadnotoria.keys())
		values = list(Enfermedadnotoria.values())

        print("las enfermedades mas notorias en el cultivo del frijol son: " + keys[values.idex(max(values))])
        print(sintomasLista)
        print(Enfermedadnotoria)
        return keys[values.idex(max(values))]


def returnSintomas(enfermedad):
	p = "";
	sintomas(enfermedad, X)
	i = 0
	for x in X.data:
		p = p + x + ", "
		i = i + 1
		if(i == 6):
			p = p + " \n "
			i = 0
	return p

def returnSintomas(plaga):
	p = "";
	sintomas(plaga, X)
	i = 0
	for x in X.data:
		p = p + x + ", "
		i = i + 1
		if(i == 3):
			p = p + " \n "
			i = 0
	return p

def returnCondicion(enfermedad):
	p = "";
	condicion(enfermedad, X)
	if len(X.data) != 0:
		for x in X.data:
			p = p + x + ", "
	else:
		p = "No hay condicion para esta enfermedad"
	return p

def returnCondicion(plaga):
	p = "";
	condicion(plaga, X)
	if len(X.data) != 0:
		for x in X.data:
			p = p + x + ", "
	else:
		p = "No hay condicion para esta plaga"
	return p

def returnDano(enfermedad):
	p = "";
	dano(enfermedad, X)
	if len(X.data) != 0:
		for x in X.data:
			p = p + x + ", "
	else:
		p = "No hay daño para esta enfermedad"
	return p

def returnDano(plaga):
	p = "";
	dano(plaga, X)
	if len(X.data) != 0:
		for x in X.data:
			p = p + x + ", "
	else:
		p = "No hay daño para esta plaga"
	return p


def returnManejo(enfermedad):
	p = "";
	manejo(enfermedad, X)
	if len(X.data) != 0:
		i = 0
		for x in X.data:
			p = p + x + ", "
			i = i + 1
			if(i == 6):
				p = p + " \n "
				i = 0				
	else:
		p = "No hay manejo para esta enfermedad"
	return p

	def returnManejo(plaga):
	    p = "";
	manejo(plaga, X)
	if len(X.data) != 0:
		i = 0
		for x in X.data:
			p = p + x + ", "
			i = i + 1
			if(i == 3):
				p = p + " \n "
				i = 0				
	else:
		p = "No hay manejo para esta plaga"
	return p



