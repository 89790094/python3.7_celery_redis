# -*- coding: utf-8 -*-

from celery_app import task

task.multiply.delay(2,4)