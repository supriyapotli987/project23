from django.shortcuts import render

# Create your views here.

from app.models import *

def display_topic(request):
   QSTO=Topic.objects.all()
   d={'QSTO':QSTO}
   return render(request,'display_topic.html',d)



def display_webpages(request):
   QSWO=Webpages.objects.all()
   d={'QSWO':QSWO}
   return render(request,'display_webpages.html',d)





def display_accessrecords(request):
   QSAO=Accessrecord.objects.all()
   d={'QSAO':QSAO}
   return render(request,'display_accessrecords.html',d)