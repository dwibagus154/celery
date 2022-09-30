from webbrowser import get
from celery import Celery
import urllib.request
import requests
import shutil
import os

BASEDIR="\downloads"

app = Celery('downloadImages',backend='rpc://',broker='amqp://guest:guest@localhost')

@app.task
def download(url,filename):
    res = requests.get(url, stream = True)
    with open(filename,'wb') as f:
        shutil.copyfileobj(res.raw, f)


@app.task
def listFile():
    return os.listdir(BASEDIR)