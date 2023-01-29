from django.shortcuts import render
from app.models import *

from django.db.models import Q
# Create your views here.

def display_topic(request):
    QST=Topic.objects.all()


    d={'Topic':QST}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    QSW=Webpage.objects.all()

    QSW=Webpage.objects.filter(name__regex='\w{5}')
    QSW=Webpage.objects.filter(name__in=['Virat Kohli','Rohit Sharma','Sunil Chhetri'])

    QSW=Webpage.objects.filter(Q(topic_name='Cricket') | Q(name='Virat Kholi'))

    QSW=Webpage.objects.filter(Q(topic_name='Cricket') & Q(url__startswith='http'))


    d={'Webpage':QSW}
    return render(request,'display_webpage.html',d)

def display_access(request):
    QSA=AccessRecord.objects.all()

    QSA=AccessRecord.objects.all().order_by('date')
    QSA=AccessRecord.objects.all()
    QSA=AccessRecord.objects.filter(date='1998-08-10')    
    QSA=AccessRecord.objects.filter(date__gt='1998-08-10')    
    QSA=AccessRecord.objects.filter(date__gte='1998-08-10') 
    QSA=AccessRecord.objects.filter(date__lte='1998-08-10')
    QSA=AccessRecord.objects.all()
    QSA=AccessRecord.objects.filter(date__year='1998')  
    QSA=AccessRecord.objects.filter(date__month='8')    
    QSA=AccessRecord.objects.filter(date__day='10')   
    QSA=AccessRecord.objects.filter(date__year__gt='1998')


    d={'AccessRecord':QSA}
    return render(request,'display_access.html',d)

def update_webpage(request):
    Webpage.objects.filter(name='K L Rahul').update(url='https://klr.in')
    Webpage.objects.filter(name='Virat Kohli').update(topic_name='Cricket')
   
    
    T=Topic.objects.get_or_create(topic_name='Cricket')[0]
    T.save()
    Webpage.objects.update_or_create(name='Rajesh',defaults={'topic_name':T,'url':'https://RJ.in'})
    Webpage.objects.update_or_create(name='Sunil Chhetri',defaults={'topic_name':T,'url':'https://sunil.in'})
    Webpage.objects.update_or_create(name='MS Dhoni',defaults={'topic_name':T,'url':'https://MSD.in'})
    Webpage.objects.filter(name='Rohit Sharma').update(topic_name='Cricket')
    Webpage.objects.update_or_create(name='Abcdefg',defaults={'topic_name':T,'url':'https://Abcdefg.in'})

    QSW=Webpage.objects.all()
    d={'webpage':QSW}
    return render(request,'display_webpage.html',d)

def delete_webpage(request):
    Webpage.objects.filter(name='Abcdefg').delete()
    #Webpage.objects.filter(topic_name='Cricket').delete()
    #Webpage.objects.filter(name='Alvarez').delete()
    #Webpage.objects.all().delete()
    QSW=Webpage.objects.all()
    d={'webpage':QSW}
    return render(request,'display_webpage.html',d)




