# signals.py

from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task
from .utils import send_task_notification

@receiver(post_save, sender=Task)
def send_task_assigned_email(sender, instance, created, **kwargs):
    """
    Send an email when a task is assigned or updated.
    """
    if created:
        subject = f"New Task Assigned: {instance.title}"
        message = render_to_string(
            'emails/task_assigned_email.html',
            {'task': instance, 'assignee': instance.assignee}
        )
        recipient_list = [instance.assignee.email]
        email = EmailMessage(subject, message, 'your-email@gmail.com', recipient_list)
        email.content_subtype = 'html'  # Set email content to HTML
        email.send(fail_silently=False)
    else:
        subject = f"Task Updated: {instance.title}"
        message = f"Hello {instance.assignee.username},\n\nThe task '{instance.title}' has been updated.\n\nDue Date: {instance.due_date}\nPriority: {instance.priority}\n\nBest regards,\nTask Manager"
        recipient_list = [instance.assignee.email]
        send_task_notification(subject, message, recipient_list)
