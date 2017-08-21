from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def Index(request):
	#return HttpResponse('Dentro de función Index')
	if request.user.is_authenticated():
		return render(request, 'Enrollment/base.html',)
	else:
		return render(request, 'Enrollment/login.html',)

def Login(request):
	#return HttpResponse('Dentro de función Index')
	return render(request, 'Enrollment/login.html',)


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