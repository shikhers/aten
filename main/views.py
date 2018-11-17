from django.shortcuts import render,get_object_or_404
from . models import Mainpage
from django.http import Http404
from django.views.generic import ListView, DetailView

def mainview(request):
    #For display data from database
    main = Mainpage.objects.order_by('-date')
    #pass objects
    context= {'main':main}
    return render(request,'index.html',context)

class Secondview(DetailView):
    #For display data from database
    model = Mainpage
    #pass objects
    context_object_name = 'batman'
    template_name = 'secondpage.html'

def Aboutview(request):
    return render(request,'about.html')

def contectview(request):
    return render(request,'contect.html')
