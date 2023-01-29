import requests
from lxml import etree
from .models import *
import random
ua = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17720', 'Mozilla/5.0 (X11; CrOS i686 0.13.507) AppleWebKit/534.35 (KHTML, like Gecko) Chrome/13.0.763.0 Safari/534.35', 'Opera/9.62 (Windows NT 5.1; U; zh-tw) Presto/2.1.1', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.459.0 Safari/534.3', 'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_5; fr-fr) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.52', 'Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; Sprint:SPH-ip320; Smartphone; 176x220)', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; de) Opera 8.01', 'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.1b3pre) Gecko/20081212 Mozilla/5.0 (Windows; U; Windows NT 5.1; en) AppleWebKit/526.9 (KHTML, like Gecko) Version/4.0dp1 Safari/526.8', 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.9200', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2) Gecko/20100305 Gentoo Firefox/3.5.7', 'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/412.6 (KHTML, like Gecko) Safari/412.2', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.198 Safari/532.0', 'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.6 Safari/532.2', 'Mozilla/4.0 (compatible; MSIE 5.0; Windows 98; YComp 5.0.2.4)', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; sv-SE; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 (.NET CLR 3.5.30729)', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.2) Gecko/20070314 Firefox/2.0.0.2', 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.13+ (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14931']
def remove_upprintable_chars(s):
    """移除所有不可见字符"""
    return ''.join(x for x in s if x.isprintable())

def get_content(my_Site,id,index):
    data = BookContent.objects.get(book_id=id).data['data']
    url = data['book_urls'][index]
    headers = {
        'User-Agent':random.choice(ua)
    }
    response = requests.get(url,headers=headers)
    response.encoding="utf-8"
    html = response.text
    ele = etree.HTML(html)
    strategy = my_Site.site_strategy
    title = ele.xpath(strategy['title'])
    article = ele.xpath(strategy['article'])
    s = ''
    for book_body in article:
            book_body = book_body.replace('\xa0\xa0\xa0\xa0\xa0\xa0\xa0', '    ')
            c = "".join(book_body.split())
            c = '\n'+remove_upprintable_chars(c)
            #print(c)
            s += c
    c = Content()
    c.title = title[0]
    c.book_id = id
    c.article = s
    c.content_id = index
    c.save()
    return s

def get_contents(my_Site,id):
    url = Book.objects.get(book_id=id).book_url
    headers = {
        'User-Agent':random.choice(ua)
    }
    response = requests.get(url,headers=headers)
    response.encoding="utf-8"
    html = response.text
    ele = etree.HTML(html)
    strategy = my_Site.site_strategy
    book_names = ele.xpath(strategy['book_names'])
    book_urls = ele.xpath(strategy['book_urls'])
    book_title = ele.xpath(strategy['book_title'])
    for i in range(len(book_urls)):
        book_urls[i] = my_Site.site_url + book_urls[i]
    data = {
        'data':{
            'book_names':book_names,
            'book_urls':book_urls,
            'book_title':book_title[0],
        }
    }
    b = BookContent()
    b.data = data
    b.book_id = id
    b.save()
    return data
