from django.shortcuts import render,redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth import authenticate,login

# Create your views here.

def get_name(request):
    if(request.user.is_authenticated()):
        return redirect('/polls')
    if (request.method == 'GET'):
        form = LoginForm()
        next_url = request.GET.get('next', '')
        return render(request, 'login/name.html', {'form' : form ,'next': next_url})
    if (request.method == 'POST'):
        next_url = request.POST.get('next', '')
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            passwd = form.cleaned_data['password']
            user = authenticate(username= uname, password = passwd)
            if user is not None:
                login(request, user)
                if next_url :
                    return redirect(next_url)
                else:
                    return redirect('/polls')
            else:
                print ("Invalid User")
                return redirect('/get_name/')


