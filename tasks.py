from celery import Celery
import time
from celery.schedules import crontab

app = Celery('tasks', backend='amqp', broker='amqp://guest@localhost//')

# @app.task
# def reverse(string):
#     return string[::-1]

# @app.task
# def update_file():
#     counter = 0
#     while True:
#         time.sleep(1)
#         with open('sample.txt','w') as f:
#             f.write(str(counter))
#         print(counter)
#         counter+=1

@app.task
def check_status():
    time.sleep(20)
    return 'Job Completed'
    

# app.conf.beat_schedule = {
#     # Executes every minute.
#     'execute-every-minute': {
#         'task': 'tasks.update_file',
#         'schedule': 30.0
#         },
# }
# app.conf.timezone = 'Europe/London'

