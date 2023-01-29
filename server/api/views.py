from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
import json, time
import api.spider

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
            'bookid':i.book_id,
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
    bookid = int(request.GET.get('book_id'))
    index = int(request.GET.get('index'))
    content = Content.objects.filter(book_id=bookid,content_id=index)
    if len(content) == 0:
        s = Book.objects.get(book_id=bookid)
        content = api.spider.get_content(s.source,bookid,index)
    else:
        content = content[0].article
    data = {
        'isSuccess': True,
        'errorMsg':'',
        'data':content,
    }
    return HttpResponse(json.dumps(data),content_type='application/json')

def getChapterList(request):
    bookid = request.GET.get('book_id')
    content = BookContent.objects.filter(book_id=bookid)
    if len(content) == 0:
        s = Book.objects.get(book_id=bookid)
        content = api.spider.get_contents(s.source,bookid)
    else:
        content = content[0].data
    content = content['data']
    contents = []
    i = 0
    for url in content['book_urls']:
        contents.append({
            'url':url,
            'title':content['book_title'][i]
        })
        i = i + 1
    data = {
        'isSuccess': True,
        'errorMsg':'',
        'data':contents,
    }
    return HttpResponse(json.dumps(data),content_type='application/json')

@csrf_exempt
def saveBookProgress(request):
    bookid = request.POST.get('book_id')
    index = request.POST.get('index')
    title = request.POST.get('title')
    b = Book.objects.get(book_id=bookid)
    b.durChapterindex = index
    b.durChapterTime = time.time()
    b.durChaptertitle = title
    b.save()
    data = {
        'isSuccess': True,
        'errorMsg':'',
        'data':title,
    }
    return HttpResponse(json.dumps(data),content_type='application/json')

# Create your views here.
