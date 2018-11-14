# coding utf-8

from celery import Celery

app = Celery('demo')

# celery加载配置模块
app.config_from_object('celery_app.conf')