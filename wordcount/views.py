from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    return render(request, 'contactus.html')

def count(request):

    fulltext = request.GET['Fulltext']
    wordlist = fulltext.split()

    return render(request, 'count.html', {"fulltext":fulltext, "count":len(wordlist)})