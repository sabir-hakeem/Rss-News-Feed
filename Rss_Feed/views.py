# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
import json
from django.views.generic.base import TemplateView
import datetime
from django.db import connection
from .models import *

import requests
from bs4 import BeautifulSoup as bs
from unidecode import unidecode
import re
# Create your views here.

class NewspageHome(TemplateView):
    ''' 
    Newsapi TemplateView
    @author: Sabir Hakeem
    '''
    def get(self, request, *args, **kwargs):
        try:
            session = requests.session()
            # the below proxy setting up is optional
            # if proxy available set up below
            # proxies = { 'https' : 'https://username:password@host:port' }
            # else set proxy to empty
            proxies = ''
            # Google Rss Feed API Url
            url = 'https://news.google.com/rss/search?pz=1&cf=all&q=$&hl=en-IN&gl=IN&ceid=IN:en'
            if proxies:
                response = session.get(url, proxies=proxies)
            else:
                response = session.get(url)
            news_data = Newsapi.objects.values('title')
            if response.status_code == 200:
                soup = bs(response.content, 'lxml')
                items = soup.find_all('item')
                cur = connection.cursor()
                for item in items:
                    title = unidecode(item.title.text)
                    link = unidecode(re.findall(r'href="(.*?)"', item.description.text)[0])
                    date = datetime.datetime.strptime(item.pubdate.text, '%a, %d %b %Y %X %Z').strftime('%Y-%m-%d %X')
                    source = unidecode(item.source.text)
                    source_link = unidecode(re.findall(r'url="(.*?)"', str(item))[0])
                    if not any(exist['title'] == title for exist in news_data):
                        insert_data = Newsapi.objects.create(title=title, title_link = link, source = source, source_link = source_link, news_date = date)
                        insert_data.save()
            final_data = Newsapi.objects.values('title', 'title_link', 'source', 'source_link', 'news_date').order_by('-news_date')
            final_data = list(final_data)
            message = 'success'
        except Exception as e:
            final_data = str(e)
            message = 'failure'
        return render(request, 'newspage.html', context ={"result":final_data, "message":message})
