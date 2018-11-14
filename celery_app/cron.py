# coding utf-8

import time
from celery_app import app

@app.task
def divide(x,y):
	time.sleep(3)
	return x/y