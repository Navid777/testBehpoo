import os

from celery import shared_task
from viewflow.flow import flow_job


@shared_task()
@flow_job()
def send_hello_world_request(activation):
    print(activation.process.text)
