from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	mykeys = {'myname':'Prateek'}
	return render(request,'rango/index.html',mykeys)
	#return HttpResponse("Hello World !") 


def about(request):
	return render(request,'rango/about.html',{})