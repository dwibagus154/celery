from webbrowser import get
from celery import Celery
import urllib.request
import requests
import shutil
import os
from time import sleep

BASEDIR="\downloads"
RABBITMQ_USERNAME="rabbitmq"
RABBITMQ_PASSWORD="rabbitmqpass"

app = Celery('downloadImages',backend='rpc://',broker='amqp://'+RABBITMQ_USERNAME+':'+RABBITMQ_PASSWORD+'@localhost')

@app.task
def download(url,filename):
    sleep(3)
    res = requests.get(url, stream = True)
    with open(filename,'wb') as f:
        shutil.copyfileobj(res.raw, f)
    return(True)


@app.task
def listFile():
    return os.listdir(BASEDIR)