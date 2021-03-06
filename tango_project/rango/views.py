from django.shortcuts import render,redirect
from django.http import HttpResponse
from rango.models import Category,Page
from rango.forms import CategoryForm,PageForm
# Create your views here.
def index(request):
	#mykeys = {'myname':'Prateek'}
	my_categories = Category.objects.all()
	context_dict = {"category_list":my_categories}
	return render(request,'rango/index.html',context_dict)
	#return HttpResponse("Hello World !") 

def category(request,category_name):
	
	#required_pages = Page.objects.filter(id=1)
	c = Category.objects.get(name=category_name)
	required_pages = c.page_set.all #c.Page.set_all()
	context_dict = {"page_objects":required_pages,"category_name":category_name}
	return render(request,'rango/category.html',context_dict)

def about(request):
	return render(request,'rango/about.html',{})

def add_category(request):
	if request.method == 'POST':
		form = CategoryForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return index(request)
		
		else:
			print form.errors
	else:
		form = CategoryForm()
	return render(request,'rango/add_category.html',{'form':form})

def add_page(request,category_name):
	cat = Category.objects.get(name=category_name)
	"""try:
		cat = Category.objects.get(name=category_name)
	except Category.DoesNotExist:
		cat = None"""

	if request.method == 'POST':
		if form.is_valid():
			if cat:
				page = form.save(commit=False)
				page.category = cat
				page.views = 0
				page.save()
				return category(request,category_name)

		else:
			print form.errors

	else:
		form = PageForm()
		context_dict = {'form':form,'category':cat}
		return render(request,'rango/add_page.html',context_dict)

