from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from django.core import serializers
import datetime
from polls.models import Question
from django.contrib.auth.decorators import login_required

# Create your views here.
def hello(request):
    print(request)
    if (request.user.is_authenticated()):
        return HttpResponse("hello"+request.user.get_full_name());
    else:
        return HttpResponse("hello world");

def current_date(request):
    now = datetime.datetime.now()
    html = "<html><head><title>Current Time</title></head><body> It is now %s </body></html>" % now
    return HttpResponse(html)

def hours_ahead(request, offset):
    print (offset)
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><head><title>Current Time</title></head><body> In %s hours, time will be  %s </body></html>" % (offset, dt)
    return HttpResponse(html)

@login_required(login_url = '/get_name/')
def get_all_questions(request):
    all_questions = Question.objects.all()
    data = serializers.serialize("json", all_questions);
    return HttpResponse(data, content_type="application/json")

def get_question(request, ques_id):
    try:
        offset = int(ques_id)
    except ValueError:
        raise Http404()
    try:
        question = Question.objects.get(pk=ques_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    data = serializers.serialize("xml", [question])
    return HttpResponse(data, content_type="application/xhtml+xml")

@login_required(login_url = '/get_name/')
def get_all_questions_template(request):
    questions = Question.objects.all()
    return render(request, 'polls/index.html', {'ques' : questions})

    
    
