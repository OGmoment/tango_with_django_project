from django.http import HttpResponse
from django.shortcuts import render



def index(request):

##    context_dict =  {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
##    return render(request,'rango/index.html',context=context_dict)
    return HttpResponse("<a href='/rango/about/'>About</a>" + "Rango says hey there partner!")



def about(request):

##    context_dict = {'boldmessage': 'This tutorial has been put together by XIANG WEi'}
##    return render(request,'rango/about.html',context=context_dict)
    
    return HttpResponse("<a href='/rango/'>Index</a>" + 'Rango says here is the about page.')