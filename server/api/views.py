from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
import json, time
import api.spider
import api.re

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
        content ,t = api.spider.get_content(s.source,bookid,index)
    else:
        content = content[0].article
    data = {
        'isSuccess': True,
        'errorMsg':'',
        'data':content,
        'i':index,
    }
    return HttpResponse(json.dumps(data),content_type='application/json')

def getChapterList(request):
    bookid = request.GET.get('book_id')
    try:
        isfresh = int(request.GET.get('isfresh'))
    except:
        isfresh=0
    bookcontent = BookContent.objects.filter(book_id=bookid)
    if len(bookcontent) == 0:
        s = Book.objects.get(book_id=bookid)
        data = api.spider.get_contents(s.source,bookid)
        content = data
        b = BookContent()
        b.data = data
        b.book_id = bookid
        b.save()
        s.latestChapterTime=time.time()
        s.latestChaptertindex=len(data['data']['book_urls'])-1 
        s.latestChaptertitle = data['data']['book_title'][-1]
        s.save()
    else:
        content = bookcontent[0].data
    if isfresh==1:
        s = Book.objects.get(book_id=bookid)
        data = api.spider.get_contents(s.source,bookid)
        bookcontent[0].data=data
        bookcontent[0].save()
        content = data
        s.latestChapterTime=time.time()
        s.latestChaptertindex=len(data['data']['book_urls'])-1 
        s.latestChaptertitle = data['data']['book_title'][-1]
        s.save()
    content = content['data']
    contents = []
    i = 0
    for url in content['book_urls']:
        if not (url[0]=='h' and url[1]=='t'):
            url = 'https://'+ url
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

def getAll(request):
    bookid = request.GET.get('bookid')
    bookcontent = BookContent.objects.filter(book_id=bookid)
    bookcontent = bookcontent[0]
    data = bookcontent.data
    contents = []
    cts = []
    for i in range(data['book_urls']):
        bookid = bookid
        index = i
        content = Content.objects.filter(book_id=bookid,content_id=index)
        if len(content) == 0:
            s = Book.objects.get(book_id=bookid)
            content ,title = api.spider.get_content(s.source,bookid,index)
        else:
            content = content[0].article
            title = content[0].title
        contents.append(content)
        cts.append(title)
    data = {
        'isSuccess': True,
        'errorMsg':'',
        'data':'',
    }
    return HttpResponse(json.dumps(data),content_type='application/json')
# Create your views here.
