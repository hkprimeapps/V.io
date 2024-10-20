from celery import Celery
from config import settings

celery = Celery('instagram_integration',
                broker=settings.CELERY_BROKER_URL,
                backend=settings.CELERY_RESULT_BACKEND)

celery.autodiscover_tasks(['tasks'])

celery = Celery('instagram_integration',
                broker=settings.CELERY_BROKER_URL,
                backend=settings.CELERY_RESULT_BACKEND,
                include=['tasks.instagram_tasks'])

celery.config_from_object('celeryconfig')
