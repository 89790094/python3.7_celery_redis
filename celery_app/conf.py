# coding:utf-8

from datetime import timedelta
from celery.schedules import crontab

# celery配置项

BROKER_URL = 'redis://:sa@192.168.199.99:6379/0'

CELERY_RESULT_BACKEND = 'redis://:sa@192.168.199.99:6379/1'

CELERY_TIMEZONE = 'Asia/Shanghai'

CELERY_IMPORTS = (
	'celery_app.task'
)

CELERYBEAT_SCHEDULE = {
	'task1':{
		'task':'celery_app.task.multiply',
		'schedule':timedelta(seconds=2),
		'args':(5,6)
	}
}

#timedelta参数：timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
#每隔一分钟运行一次：timedelta(minute=1)
#每天19:28运行一次：crontab(hour=19,minute=28)