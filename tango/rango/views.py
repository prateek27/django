from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
	#response = " Rango says: Hello world! <br/> <a href='/rango/about'>About</a>"
	context_dic ={'boldmessage':"This is bold text"}
	return render(request,'rango/index.html',context_dic)
	#return HttpResponse(response)

def about(request):
	return HttpResponse("This is the About page !")	