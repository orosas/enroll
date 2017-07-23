from django.contrib import admin
from .models import Usuario, Empresa, Enroll, Yasc

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
	pass

class EmpresaAdmin(admin.ModelAdmin):
	pass

class EnrollAdmin(admin.ModelAdmin):
	pass

class YascAdmin(admin.ModelAdmin):
	pass

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Enroll, EnrollAdmin)
admin.site.register(Yasc, YascAdmin)