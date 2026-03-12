import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'practica1_docker.settings')

app = Celery('practica1_docker')
app.config_from_object('practica1_docker.settings',namespace='CELERY')
app.autodiscover_tasks()