'''
Created on Apr 18, 2017

@author: jackwang
'''
from __future__ import absolute_import
from celery import Celery

app = Celery('SimpleCeleryProject',
             broker='amqp://jack:avtech@localhost/jack_vhost',
             backend='rpc://',
             include=['SimpleCeleryProject.tasks'])

