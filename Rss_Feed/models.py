# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Newsapi(models.Model):
    ''' 
    Newsapi Model
    @author: Sabir Hakeem
    '''
    title = models.TextField(blank=True, null=True)
    title_link = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    source_link = models.TextField(blank=True, null=True)
    news_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'news_api'
        ordering = ['id']
