import math
import os
import time

from celery import Celery

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get(
    "CELERY_BROKER_URL", "redis://localhost:6379"
)
celery.conf.result_backend = os.environ.get(
    "CELERY_BACKEND_URL", "redis://localhost:6379"
)


@celery.task(name="celery.pythagorean_theorem")
def pythagorean_theorem(x: int, y: int) -> float:
    time.sleep(60)
    z: float = math.sqrt(x**2 + y**2)
    return z
