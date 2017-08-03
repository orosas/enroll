from django.contrib import admin
from .models import Usuario, Empresa, Enroll, Yasc

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
	search_fields = ('nombres', 'apellido_paterno')

	# despliega todos éstos campos en el Admin, antes de ver detalles de cada registro
	list_display = ('nombres', 'apellido_paterno', 'status', 'empresa',)

	# agrega una barra del lado derecho para poder filtrar los resultados
	list_filter = ('empresa', 'status',)



class EmpresaAdmin(admin.ModelAdmin):
	# despliega todos éstos campos en el Admin, antes de ver detalles de cada registro
	list_display = ('nombre', 'contacto')

	# For search bar en la parte superior del admin
	search_fields = ('nombre',)

	# agrega una barra del lado derecho para poder filtrar los resultados
	#list_filter = ('nombre',)


class EnrollAdmin(admin.ModelAdmin):
	pass

class YascAdmin(admin.ModelAdmin):
	pass

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Enroll, EnrollAdmin)
admin.site.register(Yasc, YascAdmin)