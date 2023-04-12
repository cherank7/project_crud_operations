from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from django.db.models.functions import Length
# Create your views here.
def topic(request):
    to=TOPIC.objects.get_or_create(topic_name='chess')[0]
    to.save()
    return HttpResponse('inserted successfully')


def web(request):
    tn=input('enater a tname:')
    n=input('enter a name:')
    d=input('enter dob:')
    e=input('enter a email:')
    to=TOPIC.objects.get_or_create(topic_name=tn)[0]
    to.save()
    wo=WEB.objects.get_or_create(topic_name=to,name=n,dob=d,email=e)[0]
    wo.save()
    return HttpResponse('inserted successfully')
    

def display_topic(request):
    to1=TOPIC.objects.all()
    d={'names':to1}
    return render(request,'display_topic.html',context=d)


def display_web(request):
    wo1=WEB.objects.all()
    d={'details':wo1}
    wo=WEB.objects.filter(name='dhoni')
    return render(request,'display_web.html',d)

def display_web(request):

   # wo=WEB.objects.filter(name='dhoni')
    #wo=WEB.objects.filter(topic_name='cricket')
    #wo=WEB.objects.filter(name='kohli')
    wo=WEB.objects.all().order_by('name')
    wo=WEB.objects.all().order_by('-name')
    wo=WEB.objects.all().order_by(Length('name'))
    wo=WEB.objects.all().order_by(Length('name').desc())
    wo=WEB.objects.exclude(name='kohli')
   
    wo=WEB.objects.filter(dob__month='07')
    wo=WEB.objects.filter(name__startswith='d')
    wo=WEB.objects.filter(name__endswith='i')
    wo=WEB.objects.filter(name__contains='d')
    wo=WEB.objects.filter(name__startswith='d')
    o=WEB.objects.filter(dob__month='07')
    o=WEB.objects.filter(dob__day='7')


    d={'web':wo}
    return render(request,'display_web.html',d)

def display_web(request):
    wo1=WEB.objects.all()
    d={'details':wo1}
    wo1=WEB.objects.filter(name='dhoni').update(email='sakshi@gmail.com')
    wo1=WEB.objects.filter(name='kohli').update(email='virat.in')
    wo1=WEB.objects.filter(name='kohli').update(name='viratkohli')
    wo1=WEB.objects.update_or_create(name='viratkohli',defaults={'email':'viratkohli@gmail.com'})
    wo1=WEB.objects.update_or_create(name='rahul choudhary',defaults={'email':'rahul@gmail.com'})
    #wo1=WEB.objects.update_or_create(topic_name='cricket ',defaults={'email':'rahul@gmail.com'})
    to=TOPIC.objects.get_or_create(topic_name='cricket')[0]
    to.save()
    wo1=WEB.objects.update_or_create(name='hardik',defaults={'topic_name':to,'dob':'2021-02-12','email':'rahul@gmail.com'})
    d={'webpages':WEB.objects.all()}

    return render(request,'display_web.html',d)
















