from django.db import models
from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Coordinacion(models.Model):
	Cod_coordinacion = models.CharField(primary_key=True, max_length=3)
	Nombre_coordinacion = models.CharField(max_length=30)
#Duda cuanto es el largo del cod.
	def getallfields(self):
		return [self.Cod_coordinacion,self.Nombre_coordinacion]
	def __getallfieldNames__():
		return ["Cod_coordinacion","Nombre_coordinacion"]
	def __gettablename__():
		return "Coordinacion"
	def __createElement__(parameters):
		return Coordinacion(
				Cod_coordinacion = parameters["Cod_coordinacion"],
				Nombre_coordinacion = parameters["Nombre_coordinacion"]
			)

class Asignatura(models.Model):
	Cod_asignatura = models.CharField(primary_key=True, max_length=6)
	Nombre_asig = models.CharField(max_length=30)
	Cod_coordinacion = models.ForeignKey(Coordinacion, max_length=3, on_delete=models.CASCADE)
	Creditos = models.IntegerField(validators=[MaxValueValidator(30)])
	def getallfields(self):
		return [self.Cod_asignatura,self.Nombre_asig, self.Cod_coordinacion,self.Creditos]
	def __getallfieldNames__():
		return ["Cod_asignatura","Nombre_asig", "Cod_coordinacion", "Creditos"]
	def __gettablename__():
		return "Asignatura"
	def __createElement__(parameters):
		return Asignatura(
				Cod_asignatura = parameters["Cod_asignatura"],
				Nombre_asig = parameters["Nombre_asig"],
				Cod_coordinacion = parameters["Cod_coordinacion"],
				Creditos = parameters["Creditos"]
			)

class Estudiante(models.Model):
	Carnet = models.CharField(primary_key=True, max_length=8)
	Apellidos = models.CharField(max_length=30)
	Nombres = models.CharField(max_length=30)
	def getallfields(self):
		return [self.Carnet,self.Apellidos,self.Nombres]
	def __getallfieldNames__():
		return ["Carnet","Apellidos","Nombres"]
	def __gettablename__():
		return "Estudiante"
	def __createElement__(parameters):
		return Estudiante(
				Carnet = parameters["Carnet"],
				Apellidos = parameters["Apellidos"],
				Nombres = parameters["Nombres"]
			)

class Profesor(models.Model):
	Id_prof = models.CharField(primary_key=True, max_length=7)
	Apellidos = models.CharField(max_length=30)
	Nombres = models.CharField(max_length=30)
	Cod_coordinacion = models.ForeignKey(Coordinacion, max_length=3, on_delete=models.CASCADE)
	def getallfields(self):
		return [self.Id_prof,self.Apellidos,self.Nombres,self.Cod_coordinacion]
	def __getallfieldNames__():
		return ["Id_prof","Apellidos","Nombres","Cod_coordinacion"]
	def __gettablename__():
		return "Profesor"
	def __createElement__(parameters):
		return Profesor(
				Id_prof = parameters["Id_prof"],
				Apellidos = parameters["Apellidos"],
				Nombres = parameters["Nombres"],
				Cod_coordinacion = parameters["Cod_coordinacion"]
			)

class Trimestre(models.Model):
	class Meta:
		unique_together = (('Periodo', 'Anio'))
	Periodo = models.CharField(max_length=20)
	Anio = models.IntegerField(validators=[MaxValueValidator(9999)])
	def getallfields(self):
		return [self.Periodo,self.Anio]
	def __getallfieldNames__():
		return ["Periodo","Anio"]
	def __gettablename__():
		return "Trimestre"
	def __createElement__(parameters):
		return Trimestre(
				Periodo = parameters["Periodo"],
				Anio = parameters["Anio"]
			)

class Cursa(models.Model):
	class Meta:
		unique_together=(('Carnet', 'Cod_asignatura', 'Periodo', 'Anio'))
	Carnet = models.ForeignKey(Estudiante, primary_key=True, on_delete=models.CASCADE)
	Cod_asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
	Periodo = models.ForeignKey(Trimestre, related_name='Trimestre_cursa_periodo', on_delete=models.CASCADE)
	Anio = models.ForeignKey(Trimestre, related_name='Trimestre_cursa_anio', on_delete=models.CASCADE)
	def getallfields(self):
		return [self.Carnet,self.Cod_asignatura,self.Periodo,self.Anio]
	def __getallfieldNames__():
		return ["Carnet","Cod_asignatura","Periodo","Anio"]
	def __gettablename__():
		return "Cursa"
	def __createElement__(parameters):
		return Cursa(
				Carnet = parameters["Carnet"],
				Cod_asignatura = parameters["Cod_asignatura"],
				Periodo = parameters["Periodo"],
				Anio = parameters["Anio"]
			)

class Se_Ofrece(models.Model):
	class Meta:
		unique_together = (('Id_prof', 'Cod_asignatura','Horario', 'Periodo', 'Anio'))
	Id_prof = models.ForeignKey(Profesor, primary_key=True, on_delete=models.CASCADE)
	Cod_asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
	Horario = models.CharField(max_length=5)
	Periodo = models.ForeignKey(Trimestre, related_name='Trimestre_ofrece_periodo', on_delete=models.CASCADE)
	Anio = models.ForeignKey(Trimestre, related_name='Trimestre_ofrece_anio', on_delete=models.CASCADE)
	def getallfields(self):
		return [self.Id_prof,self.Cod_asignatura,self.Horario,self.Periodo,self.Anio]
	def __getallfieldNames__():
		return ["Id_prof","Cod_asignatura","Horario","Periodo","Anio"]
	def __gettablename__():
		return "Se_Ofrece"
	def __createElement__(parameters):
		return Se_Ofrece(
				Id_prof = parameters["Id_prof"],
				Cod_asignatura = parameters["Cod_asignatura"],
				Horario = parameters["Horario"],
				Periodo = parameters["Periodo"],
				Anio = parameters["Anio"]
			)


class MedioPago(models.Model):
	Postiza = models.AutoField(primary_key=True)
	def getallfields(self):
		return [self.Postiza]
	def __getallfieldNames__():
		return ["Postiza"]
	def __gettablename__():
		return "MedioPago"
	def __createElement__(parameters):
		return MedioPago(
				Postiza=parameters["Postiza"]
			)

class Paga_Con(models.Model):
	class Meta:
		unique_together = (('Carnet', 'Postiza', 'Periodo', 'Anio'))
	Precio = models.DecimalField(max_digits=19, decimal_places=4)
	Carnet = models.ForeignKey(Estudiante, primary_key=True, on_delete=models.CASCADE)
	Postiza = models.ForeignKey(MedioPago, on_delete=models.CASCADE)
	Periodo = models.ForeignKey(Trimestre, related_name='Trimestre_pago_periodo', on_delete=models.CASCADE)
	Anio = models.ForeignKey(Trimestre, related_name='Trimestre_pago_anio', on_delete=models.CASCADE)
	def getallfields(self):
		return [self.Precio,self.Carnet,self.Cod_asignatura,self.Periodo,self.Anio]
	def __getallfieldNames__():
		return ["Precio","Carnet","Cod_asignatura","Periodo","Anio"]
	def __gettablename__():
		return "Paga_Con"
	def __createElement__(parameters):
		return Paga_Con(
				Precio = parameters["Precio"],
				Carnet = parameters["Carnet"],
				Postiza = parameters["Postiza"],
				Periodo = parameters["Periodo"],
				Anio = parameters["Anio"]
			)

class Debito(models.Model):
	Nro_Cuenta = models.IntegerField(primary_key=True,validators=[MaxValueValidator(99999999999999999999)])
	Nro_Tarjeta = models.IntegerField(validators=[MaxValueValidator(999999999999999999)])
	Tipo = models.CharField(max_length=9)
	Nombre_Banco = models.CharField(max_length=30)
	Postiza = models.ForeignKey(MedioPago, on_delete=models.CASCADE)
	def getallfields(self):
		return [self.Nro_Cuenta,self.Nro_Tarjeta,self.Tipo,self.Nombre_Banco,self.Postiza]
	def __getallfieldNames__():
		return ["Nro_Cuenta","Nro_Tarjeta","Tipo","Nombre_Banco","Postiza MedioPago"]
	def __gettablename__():
		return "Debito"
	def __createElement__(parameters):
		return Debito(
				Nro_Cuenta = parameters["Nro_Cuenta"],
				Nro_Tarjeta = parameters["Nro_Tarjeta"],
				Tipo = parameters["Tipo"],
				Nombre_Banco = parameters["Nombre_Banco"],
				Postiza = parameters["Postiza"]
			)

class Credito(models.Model):
	Nro_Tarjeta = models.IntegerField(primary_key=True,validators=[MaxValueValidator(999999999999999999)])
	Fecha_Vence = models.DateField() 
	Nombre_Banco = models.CharField(max_length=30)
	Postiza = models.ForeignKey(MedioPago, on_delete=models.CASCADE)
	def getallfields(self):
		return [self.Nro_Tarjeta,self.Fecha_Vence,self.Nombre_Banco,self.Postiza]
	def __getallfieldNames__():
		return ["Nro_Tarjeta","Fecha_Vence","Nombre_Banco","Postiza MedioPago"]
	def __gettablename__():
		return "Credito"
	def __createElement__(parameters):
		return Credito(
				Nro_Tarjeta = parameters["Nro_Tarjeta"],
				Fecha_Vence = parameters["Fecha_Vence"],
				Nombre_Banco = parameters["Nombre_Banco"],
				Postiza = parameters["Postiza"]
			)

class Transferencia(models.Model):
	Nro_Referencia = models.IntegerField(primary_key=True, validators=[MaxValueValidator(99999999999999999999)])
	Postiza = models.ForeignKey(MedioPago, on_delete=models.CASCADE)
	def getallfields(self):
		return [self.Nro_Referencia,self.Postiza]
	def __getallfieldNames__():
		return ["Nro_Referencia","Postiza MedioPago"]
	def __gettablename__():
		return "Transferencia"
	def __createElement__(parameters):
		return Debito(
				Nro_Referencia = parameters["Nro_Referencia"],
				Postiza = parameters["Postiza"]
			)

class Deposito(models.Model):
	Referencia = models.IntegerField(primary_key=True, validators=[MaxValueValidator(99999999999999999999)])
	Postiza = models.ForeignKey(MedioPago, on_delete=models.CASCADE)
	def getallfields(self):
		return [self.Referencia,self.Postiza]
	def __getallfieldNames__():
		return ["Referencia","Postiza MedioPago"]
	def __gettablename__():
		return "Deposito"
	def __createElement__(parameters):
		return Debito(
				Referencia = parameters["Referencia"],
				Postiza = parameters["Postiza"]
			)