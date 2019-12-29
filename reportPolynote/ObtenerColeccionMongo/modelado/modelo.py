'''
	Autor: Carlos Castillo
'''

class Persona(object):

	def __init__(self,cedula,nombres,apellidos,edad,mail,telefono):

		self.establecerCedula(cedula)
		self.establecerNombres(nombres)
		self.establecerApellidos(apellidos)
		self.establecerEdad(edad)
		self.establecerMail(mail)
		self.establecerTelefono(telefono)

	def __str__(self):
		return ("Cedula: %s - Nombres: %s - Apellidos: %s - Edad: %d - Mail: %s - Telefono: %s\n"%(self.obtenerCedula(),
			self.obtenerNombres(),self.obtenerApellidos(),self.obtenerEdad(),self.obtenerMail(),self.obtenerTelefono()) )


	#Retorna los datos en formato diccionario 
	def obtenerDBColeccion(self):
		return {
			"cedula": self.obtenerCedula(),
			"nombres": self.obtenerNombres(),
			"apellidos": self.obtenerApellidos(),
			"edad": self.obtenerEdad(),
			"mail": self.obtenerMail(),
			"telefono": self.obtenerTelefono()
		}
	
	# Metodos Set
	def establecerCedula(self,cedula):
		self.cedula = cedula

	def establecerNombres(self,nombres):
		self.nombres = nombres

	def establecerApellidos(self, apellidos):
		self.apellidos = apellidos

	def establecerEdad(self, edad):
		self.edad = int(edad)

	def establecerMail(self, mail):
		self.mail = mail

	def establecerTelefono(self, telefono):
		self.telefono = telefono

	# Metodos Get

	def obtenerCedula(self):
		return self.cedula

	def obtenerNombres(self):
		return self.nombres

	def obtenerApellidos(self):
		return self.apellidos

	def obtenerEdad(self):
		return self.edad

	def obtenerMail(self):
		return self.mail

	def obtenerTelefono(self):
		return self.telefono



