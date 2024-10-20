from celery.schedules import crontab

beat_schedule = {
    'refresh-instagram-tokens': {
        'task': 'app.tasks.instagram_tasks.refresh_all_tokens',
        'schedule': crontab(hour='*/1'),  # Every hour
    },
}
