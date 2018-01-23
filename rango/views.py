from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    context_dict = {'boldmessage': "Crunch, creamy, cookie, candy, cupcake!"}

    return render(request, 'rango/index.html', context=context_dict)
    return HttpResponse("Rango says hey there partner!")
    

def about(request):

    context_dict = {'boldmessage': "ABOUT PAGE"}
    
    return render(request, 'rango/about.html', context=context_dict)
    return HttpResponse("Rango says here is the about page")
