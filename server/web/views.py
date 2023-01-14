from django.shortcuts import render

def index(request):
    return render(request, 'web/index.html')

def reader(request):
    content = request.GET.get('id',default='1')
    url = request.GET.get('url',default='1')
    name = request.GET.get('n',default='1')
    context = {
        'content':content,
        'url':url,
        'name':name,
    }
    return render(request, 'web/reader.html', context)