from webbrowser import get
from celery import Celery
import urllib.request
import requests
import shutil
import os
from time import sleep, time

BASEDIR="\downloads"
RABBITMQ_USERNAME="guest"
RABBITMQ_PASSWORD="guest"

app = Celery('download',backend='rpc://',broker='amqp://'+RABBITMQ_USERNAME+':'+RABBITMQ_PASSWORD+'@localhost')

app.conf.beat_schedule = {
    'add-every-3-seconds': {
        'task': 'downloads',
        'schedule': 3.0
    },
}
app.conf.timezone = 'UTC'


@app.task(name='downloads')
def download():
	url = "https://i.pinimg.com/564x/0e/d6/23/0ed623806cf3b9d805a8cb1e4c822daf.jpg"
	filename = "contoh" + str(time()) + ".png"
	sleep(3)
	res = requests.get(url, stream = True)
	with open(filename,'wb') as f:
		shutil.copyfileobj(res.raw, f)
	return(True)
   


@app.task
def listFile():
    return os.listdir(BASEDIR)