from celery import shared_task
import time

@shared_task
def tarea_prueba():
    print('Iniciando tarea...')
    time.sleep(5)
    print('Tarea Finalizado')