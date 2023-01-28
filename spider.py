import requests
import re
from lxml import etree
url = "http://www.quanzhifashi.com/novel/75441/"
response = requests.get(url)
response.encoding="utf-8"

html = response.text


#ele
ele = etree.HTML(html)
book_names = ele.xpath("/html/body/div[1]/div[4]/div[1]/div[2]/ul/li/a/text()")
book_urls = ele.xpath("/html/body/div[1]/div[4]/div[1]/div[2]/ul/li/a/@href")

from tqdm import tqdm



chapter_titles = book_names
chapter_urls = book_urls
def remove_upprintable_chars(s):
    """移除所有不可见字符"""
    return ''.join(x for x in s if x.isprintable())
import time
o_url = "http://www.quanzhifashi.com"
#new_url =  o_url +  chapter_urls[0]
pbar = tqdm(range(len(chapter_urls)))
for i in pbar:
     new_url =  o_url +  chapter_urls[i]

     #print(new_url)
     try:
        try:
            response = requests.get(new_url)
        except:
            time.sleep(10)
            response = requests.get(new_url)
        response.encoding="utf-8"
        html = response.text
        #print(html)
        ele = etree.HTML(html)
        book_bodys = ele.xpath("//*[@id='articlecontent']/p/text()")
        #print(book_bodys[0])
        s = chapter_titles[i]
        #print(book_bodys)
        for book_body in book_bodys:
            book_body = book_body.replace('\xa0\xa0\xa0\xa0\xa0\xa0\xa0', '    ')
            c = "".join(book_body.split())
            c = '\n'+remove_upprintable_chars(c)
            #print(c)
            s += c
        with open("我变成美少女.txt","a",encoding='utf-8') as f:
            f.write(s)
     except:
        pass
        
print("文章《牧神记》 下载完毕！")


