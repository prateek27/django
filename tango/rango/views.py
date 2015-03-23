from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category,Page

# Create your views here.
def index(request):
	#response = " Rango says: Hello world! <br/> <a href='/rango/about'>About</a>"
	#context_dic ={'boldmessage':"This is bold text"}
	category_list = Category.objects.all()
	context_dict ={'categories':category_list}
	return render(request,'rango/index.html',context_dict)
	#return HttpResponse(response)

def about(request):
	return HttpResponse("This is the About page !")	