from django.shortcuts import render

def index(request):
    return render(request, 'web/index.html')

def reader(request):
    return render(request, 'web/reader.html')