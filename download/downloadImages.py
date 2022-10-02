from webbrowser import get
from celery import Celery
from celery.exceptions import SoftTimeLimitExceeded
import urllib.request
import requests
import shutil
import os
from time import sleep

BASEDIR="\downloads"
RABBITMQ_USERNAME="guest"
RABBITMQ_PASSWORD="guest"

app = Celery('downloadImages',backend='rpc://',broker='amqp://'+RABBITMQ_USERNAME+':'+RABBITMQ_PASSWORD+'@localhost')

@app.task(bind=True,time_limit=10, max_retries=3, default_retry_delay=5)
def download(self, url,filename):
    try:
        sleep(3)
        res = requests.get(url, stream = True)
        with open(filename,'wb') as f:
            shutil.copyfileobj(res.raw, f)
        return(True)
    except SoftTimeLimitExceeded:
        self.retry(countdown=5)
    


@app.task
def listFile():
    return os.listdir(BASEDIR)