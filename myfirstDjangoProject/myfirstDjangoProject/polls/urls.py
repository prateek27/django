from django.conf.urls import patterns, include, url
from polls import views
from polls.views import hello, current_date, hours_ahead, get_all_questions, get_question,get_all_questions_template

urlpatterns = patterns('',
    url(r'^hello/$', hello),
    url(r'$', get_all_questions_template),
    url(r'^time/plus/(?P<offset>[A-Z\d]{1,2})/$', hours_ahead),
    url(r'^current_time/$', current_date),
    url(r'^server-time/$', current_date),
    url(r'^questions/$', get_all_questions),
    url(r'^questions/(?P<ques_id>\d+)/$', get_question)


    )
