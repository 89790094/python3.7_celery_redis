# coding:utf-8

# celery配置项

BROKER_URL = 'redis://:sa@192.168.199.99:6379/0'

CELERY_RESULT_BACKEND = 'redis://:sa@192.168.199.99:6379/1'

CELERY_TIMEZONE = 'Asia/Shanghai'

CELERY_IMPORTS = (
	'celery_app.task'
)