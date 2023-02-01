from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models import Q
from django.db.models.functions import Length
def insert_topic(request):
    QST=Topic.objects.all()
    QST=Topic.objects.filter(topic_name='cricket')
    d={'topics':QST}
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(topic_name='kabaddi')
    QSW=Webpage.objects.exclude(topic_name='kabaddi')
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(name__startswith='d')
    QSW=Webpage.objects.filter(url__endswith='in')
    QSW=Webpage.objects.filter(name__contains='s')
    QSW=Webpage.objects.filter(name__regex='\w{7}')
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(name__in=['msd','ronaldo','rahul'])
    QSW=Webpage.objects.filter(Q(topic_name='cricket') | Q(url='htttp'))
    QSW=Webpage.objects.all()
    #QSW=Webpage.objects.filter(Q(topic_name='cricket') & Q(url='https'))
    QSW=Webpage.objects.all().order_by('name')
    QSW=Webpage.objects.all().order_by('-name')
    #QSW=Webpage.objects.all().order_by('name')
    QSW=Webpage.objects.all().order_by(Length('name'))
    QSW=Webpage.objects.all().order_by(Length('name').desc())
    d={'webpage':QSW}
    return render(request,'insert_webpage.html',d)
def insert_Accessrecords(request):
    QSA=Accessrecords.objects.all()
    QSA=Accessrecords.objects.filter(date='2023-01-30')
    QSA=Accessrecords.objects.filter(date__gt='2021-09-14')
    QSA=Accessrecords.objects.filter(date__gte='2023-01-30')
    QSA=Accessrecords.objects.filter(date__lt='2023-01-30')
    QSA=Accessrecords.objects.filter(date__lte='2023-01-13')
    QSA=Accessrecords.objects.all()
    QSA=Accessrecords.objects.filter(date__year='2023')
    QSA=Accessrecords.objects.filter(date__month='09')
    QSA=Accessrecords.objects.filter(date__day='30')
    QSA=Accessrecords.objects.filter(date__day__gt='13')
    d={'Accessrecords':QSA}
    return render(request,'insert_Accessrecords.html',d)



def update_webpage(request):
    #Webpage.objects.filter(name='msd').update(url='http://msd.com')
    #Webpage.objects.filter(name='dinesh').update(topic_name='cricket')
    #Webpage.objects.filter(name='adc').update(topic_name='kabadddi')
    #Webpage.objects.filter(topic_name='cricket').update(name='hardhik')
    #Webpage.objects.update_or_create(name='dinesh',defaults={'url':'https://dinesh.in'})
    #Webpage.objects.update_or_create(name='rahul',defaults={'url':'.com'})
    #Webpage.objects.update_or_create(name='harry',defaults={'topic_name':'rugby'})
    
    QSW=Webpage.objects.all()
    d={'webpage':QSW}
    return render(request,'insert_webpage.html',d)
def delete_Access(request):
    Accessrecords.objects.filter(date='2023-01-25').delete()
    QSA=Accessrecords.objects.all()
    d={'Accessrecords':QSA}
    return render(request,'insert_Accessrecords.html',d)



    