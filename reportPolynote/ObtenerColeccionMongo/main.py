
'''
	Autor: Carlos Castillo
'''
from pymongo import MongoClient
from modelado.modelo import Persona


listaPersonas = [
	Persona('1104999535','Carlos Andres','Castillo Giron','20','cacastillo19@utpl.edu.ec','0939650879'),
	Persona('1105025387','Thalia Lilibeth','Mijas Abad','24','tlmijas@utpl.edu.ec','0986922823'),
	Persona('1102721238','Jose Wilmer','Castillo Torres','56','jwcastillo@utpl.edu.ec','0912879032'),
	Persona('1105031551','Karen Maritza','Castillo Giron','19','kmcastillo@utpl.edu.ec','0988020612'),
	Persona('1106048620','Brandon Ismael','Cueva Velez','20','bicueva@utpl.edu.ec','0998133022')
]

mongoClient = MongoClient('localhost',27017) # Conexion al Server de MongoDB
db = mongoClient.Persona # Conexion con la base de datos
coleccion = db.Personas # Obtener una coleccion para trabajar con ella

# CREATE 
for persona in listaPersonas:
	coleccion.insert(persona.obtenerDBColeccion()) # Insertamos en la coleccion los objetos tipo persona

cursor = coleccion.find() # Leemos todos los datos de la coleccion

for x in cursor:
	print("%s - %s - %s - %s - %s - %s" %(x['cedula'],x['nombres'],
		x['apellidos'],x['edad'],x['mail'],x['telefono']))