import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sending_app.settings')

app = Celery('sending_app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'check_every_1_minute': {
        'task': 'mailing_list.tasks.check_mailing',
        'schedule': crontab(minute='*/1')
    }
}