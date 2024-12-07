from celery import shared_task
from django.core.mail import send_mail
from django_app.models import EmailMessage

@shared_task
def send_email_task(subject, message, recipient_list):
    send_mail(
        subject,
        message,
        'sarsendimas@gmail.com',
        recipient_list,
        fail_silently=False,
    )
    EmailMessage.objects.create(
        subject=subject,
        message=message,
        recipients=', '.join(recipient_list),
    )
