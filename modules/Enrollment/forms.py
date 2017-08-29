from django import forms

class BusquedaForm(forms.Form):
	q = forms.CharField(max_length=80)