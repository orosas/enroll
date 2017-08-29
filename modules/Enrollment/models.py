from django.db import models
from django.contrib.auth.models import User


# Create your models here.

STATUS_EMPRESA = (
	('AC','Activa'),
	('BJ','Baja'),
	)

class Empresa(models.Model):
	nombre = models.CharField(max_length=100, null=False, blank=False)
	contacto = models.CharField(max_length=50, null=True, blank=True)
	email = models.EmailField(max_length=50, null=True, blank=True)
	telefono = models.CharField(max_length=50, null=True, blank=True)
	status_empresa = models.CharField(choices=STATUS_EMPRESA, max_length=2)
	fecha_modif = models.DateField(auto_now=True)
	fecha_creacion = models.DateField(auto_now_add=True)
	capturado_por_usuario = models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return u"%s" % (self.nombre)

STATUS = (
	('AC','Activo'),
	('BJ','Baja'),
	('BL','Bloqueado'),
	('PR','En Proceso'),
	)

STATUS_OPERACIONES = (
	('OP','Operativo'),
	('SP','En Espera De Asignación'),
	)

CARGO = (
	('AD','Administrativo'),
	('CO','Coordinador'),
	('LI','Líder'),
	('PM','PM'),
	('SP','Supervisor'),
	('TC','Técnico'),
	)

# Si se requiere que un campo almace varias opciones como choices
# Se hace desde forms.py 
'''
<forms.py>

class SomeForm(forms.Form):
    CHOICES = (('a','a'),
               ('b','b'),
               ('c','c'),
               ('d','d'),)
    picked = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple())
'''

class Usuario(models.Model):
	nombres = models.CharField(max_length=50, null=False, blank=False)
	apellido_paterno = models.CharField(max_length=50, null=False, blank=False)
	apellido_materno = models.CharField(max_length=50, null=False, blank=False)
	empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
	status = models.CharField(choices=STATUS, max_length=2)
	status_operaciones = models.CharField(choices=STATUS_OPERACIONES, max_length=2, null=True, blank=True)
	fecha_baja = models.DateField(null=True, blank=True)
	observaciones = models.TextField(null=True, blank=True)
	email = models.EmailField(max_length=100, null=True, blank=True)
	telefono = models.CharField(max_length=200, null=True, blank=True)
	num_imss = models.CharField(max_length=11, null=True, blank=True)
	curp = models.CharField(max_length=18, null=True, blank=True)
	direccion = models.TextField(null=True, blank=True)
	cargo = models.CharField(choices=CARGO, max_length=2, null=True, blank=True)
	# Campo para guardar diversas actividades que ejecuta el usuario
	# por ejemplo Civil Works, I&C, Decomisionamiento
	# las opciones se definen en el form
	actividades = models.TextField(null=True, blank=True)
	fecha_liberado_ehs = models.DateField(null=True, blank=True)
	u_fecha_modificacion = models.DateField(auto_now=True)
	u_fecha_creacion = models.DateField(auto_now_add=True)
	capturado_por = models.ForeignKey(User, on_delete=models.CASCADE,)

	def __str__(self):
		return u"%s %s %s" % (self.nombres, self.apellido_paterno, self.apellido_materno)

class Enroll(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE,)
	acuse_att = models.PositiveIntegerField(null=True, blank=True)
	enrollment_id = models.CharField(max_length=6, null=False, blank=False)
	comentario = models.TextField(null=False, blank=False)
	fecha_aprobacion = models.DateField(null=True, blank=True)
	fecha_modif = models.DateField(auto_now=True)
	fecha_creacion = models.DateField(auto_now_add=True)
	captura_por = models.ForeignKey(User, on_delete=models.CASCADE,)

	def __str__(self):
		return u"%s" % (self.acuse_att)

class Yasc(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE,)
	password = models.CharField(max_length=50, null=False, blank=False)
	imei = models.CharField(max_length=17, null=True, blank=True)
	pac_blu = models.DateField(null=True, blank=True)
	email_pac_blu = models.CharField(max_length=60, null=False, blank=False)
	comentario = models.TextField(null=False, blank=False)
	fecha_modificacion = models.DateField(auto_now=True)
	fecha_creacion = models.DateField(auto_now_add=True)
	capturado_por = models.ForeignKey(User, on_delete=models.CASCADE,)

	def __str__(self):
		return u"%s" % (self.imei)

class Epp(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE,)
	dc3_alturas = models.DateField(null=True, blank=True)
	dc3_escaleras = models.DateField(null=True, blank=True)
	dc3_riesgos_electricos = models.DateField(null=True, blank=True)
	primeros_auxilios = models.DateField(null=True, blank=True)
	certificado_medico = models.DateField(null=True, blank=True)
	arnes = models.DateField(null=True, blank=True)
	bandola = models.DateField(null=True, blank=True)
	linea_vida = models.DateField(null=True, blank=True)

	def __str__(self):
		return u"%s" % (self.usuario)
