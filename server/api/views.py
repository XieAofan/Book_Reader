from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import json
import spider

data = {
        'isSuccess': True,
        'errorMsg':'',
        'data':{}
    }

def getBookshelf(request):
    data = {
        'isSuccess': True,
        'errorMsg':'',
        'data':[]
    }
    for i in list(Book.objects.all()):
        books = {
            'name':i.name,
            'author':i.author,
            'bookid':i.author,
            'bookUrl':i.book_url,
            'coverUrl':i.coverUrl,
            'durChapterTitle':i.durChaptertitle,
            'durChapterIndex':int(i.durChapterindex),
            'durChapterTime':int(i.durChapterTime),
            'latestChapterTitle':i.latestChaptertitle,
            'latestChaptertIndex':int(i.latestChaptertindex),
            'latestChapterTime':int(i.latestChapterTime),
        }
        data['data'].append(books)
    return HttpResponse(json.dumps(data),content_type='application/json')

def getBookContent(request):
    bookid = request.GET.get('book_id')
    index = request.GET.get('index')
    content = Content.objects.filter(book_id=bookid,index=index)
    content = list(content)
    if len(content) == 0:
        spider.get_content
    data = {
        'isSuccess': True,
        'errorMsg':'',
        'data':content,
    }

# Create your views here.
