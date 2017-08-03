from django.db import models
from django.contrib.auth.models import User


class Empresa(models.Model):
	nombre = models.CharField(max_length=100, null=False, blank=False)
	contacto = models.CharField(max_length=50, null=True, blank=True)
	email = models.EmailField(max_length=50, null=True, blank=True)
	telefono = models.CharField(max_length=50, null=True, blank=True)
	fecha_modif = models.DateField(auto_now=True)
	fecha_creacion = models.DateField(auto_now_add=True)
	autor = models.ForeignKey(User,related_name='eluser')

	def __str__(self):
		return u"%s" % (self.nombre)


# Create your models here.

STATUS = (
	('AC','Activo'),
	('BJ','Baja'),
	('BN','Baja Network'),
	('BL','Bloqueado'),
	('PE','Pendiente'),
	('RE','Rechazado'),
	('RS','Revisar Estatus'),
	)


class Usuario(models.Model):
	nombres = models.CharField(max_length=50, null=False, blank=False)
	apellido_paterno = models.CharField(max_length=50, null=False, blank=False)
	apellido_materno = models.CharField(max_length=50, null=False, blank=False)
	empresa = models.ForeignKey(Empresa, related_name='laempresa')
	status = models.CharField(choices=STATUS, max_length=2)
	fecha_baja = models.DateField(null=True, blank=True)
	email = models.EmailField(max_length=100, null=False, blank=False)
	telefono = models.CharField(max_length=200, null=False, blank=False)
	num_imss = models.CharField(max_length=11, null=False, blank=False)
	curp = models.CharField(max_length=18, null= False, blank=False)
	direccion = models.TextField(null=False, blank=False)
	u_fecha_modificacion = models.DateField(auto_now=True)
	u_fecha_creacion = models.DateField(auto_now_add=True)
	autor = models.ForeignKey(User,related_name='elusuario')

	def __str__(self):
		return u"%s %s %s" % (self.nombres, self.apellido_paterno, self.apellido_materno)

class Enroll(models.Model):
	usuario = models.ForeignKey(Usuario, related_name='elenrollment')
	acuse_att = models.PositiveIntegerField(null=True, blank=True)
	enrollment_id = models.CharField(max_length=6, null=False, blank=False)
	comentario = models.TextField(null=False, blank=False)
	fecha_aprobacion = models.DateField(null=True, blank=True)
	fecha_modif = models.DateField(auto_now=True)
	fecha_creacion = models.DateField(auto_now_add=True)

	def __str__(self):
		return u"%s" % (self.acuse_att)

class Yasc(models.Model):
	usuario = models.ForeignKey(Usuario, related_name='elenrollment2')
	password = models.CharField(max_length=50, null=False, blank=False)
	imei = models.CharField(max_length=17, null=True, blank=True)
	email = models.CharField(max_length=50, null=False, blank=False)
	comentario = models.TextField(null=False, blank=False)
	fecha_modificacion = models.DateField(auto_now=True)
	fecha_creacion = models.DateField(auto_now_add=True)

	def __str__(self):
		return u"%s" % (self.imei)