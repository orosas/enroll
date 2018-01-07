from django.shortcuts import render

from .models import Usuario, Empresa
from django.db.models import Q

from .forms import BusquedaForm
#from django.http import HttpResponse

# Create your views here.
def Index(request):
	#return HttpResponse('Dentro de función Index')
	if request.user.is_authenticated():
		form = BusquedaForm()
		return render(request, 'Enrollment/index.html', {'form': form})
	else:
		return render(request, 'Enrollment/login.html',)

def Login(request):
	#return HttpResponse('Dentro de función Index')
	return render(request, 'Enrollment/login.html',)


# Recibe string desde formulario para buscar
# Usuario o usuarios de una empresa
# regresa resultados a template res_busqueda_usuario.html
def Busqueda(request):


	if request.method == 'POST':
		#print("Dentro de request.method: **************")
		form = BusquedaForm(request.POST)
		error_res_q = False

		if form.is_valid():
			#print("************* Dentro de form.is_valid")
			q = form.cleaned_data['q']

			#con Q(empresa__nombre__unaccent__icontains=q) se hace una búsqueda "cruzada" en el modelo Empresa y campo nombre
            # al mismo tiempo que en Usuario.objects
			#print("El q: " + q)
			res_q_usuario = Usuario.objects.filter(Q(nombres__unaccent__icontains=q)|
															Q(apellido_paterno__unaccent__icontains=q)|
															Q(apellido_materno__unaccent__icontains=q)|
                                                            Q(empresa__nombre__unaccent__icontains=q)
												)
			cant_resultados = res_q_usuario.count()
			
            # En caso de que no haya resultados en la búsqueda del query
            # se envía error
			if not res_q_usuario:
				#print("Hay error en la búsqueda. ¡¡¡¡¡¡¡¡¡")
				error_res_q = True
				return render(request, 'Enrollment/res_busqueda_usuario.html', {'form': form,
                                                                                'elerror': error_res_q,},
                             )

			#print("antes de for resultado in: 222222222222222222")
			#print(res_q_usuario)
			'''
			print("<<<<< res_q_usuario.count: " + str(res_q_usuario.count()))
			cant_resultados = res_q_usuario.count()
			for resultado in res_q_usuario:
				print(" <<<<<<<<<< dentro de for que no se ve >>>>>>>>>>>>><")
				print("Usuario PK: " + str(resultado.pk))
				print("Usuario empresa: " + str(resultado.empresa))
			'''

	return render(request, 'Enrollment/res_busqueda_usuario.html', {'form': form,
														'elerror': error_res_q,
														'cant_resultados': cant_resultados,
														'q':q,
                                                        'usuarios':res_q_usuario,
                                                        }
				)

'''
	ToDo:
*************************************************************************
		Para subir archivos:
		https://docs.djangoproject.com/en/1.11/topics/http/file-uploads/

		Checar si un directorio existe o crear uno:
		import os
		print(os.path.isdir("/home/el"))
		print(os.path.exists("/home/el/myfile.txt"))


		forms.py <<<<<<<<<<<<
		from django import forms

		class UploadFileForm(forms.Form):
		    title = forms.CharField(max_length=50)
		    file = forms.FileField()


		views.py <<<<<<<<<<
		from django.http import HttpResponseRedirect
		from django.shortcuts import render
		from .forms import UploadFileForm

		# Imaginary function to handle an uploaded file.
		from somewhere import handle_uploaded_file

		def upload_file(request):
		    if request.method == 'POST':
		        form = UploadFileForm(request.POST, request.FILES)
		        if form.is_valid():
		            handle_uploaded_file(request.FILES['file'])
		            return HttpResponseRedirect('/success/url/')
		    else:
		        form = UploadFileForm()
		    return render(request, 'upload.html', {'form': form})


		def handle_uploaded_file(f):
		    with open('some/file/name.txt', 'wb+') as destination:
		        for chunk in f.chunks():
		            destination.write(chunk)
*************************************************************************
'''
