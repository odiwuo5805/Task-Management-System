# utils.py

from django.core.mail import send_mail
from django.conf import settings

def send_task_notification(subject, message, recipient_list):
    """
    Send email notification for task assignments or updates.
    """
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,  # From email (configured in settings)
        recipient_list,  # List of recipients
        fail_silently=False,
    )
