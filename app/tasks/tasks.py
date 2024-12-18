from pydantic import EmailStr
import smtplib

from app.tasks.celery_app import celery
from app.config import settings
from app.tasks.email_templates import create_booking_confirmation_template


@celery.task
def email_rent_confirm(
    rent: dict,
    good: dict,
    email_to: EmailStr
):
    msg_content = create_booking_confirmation_template(rent, good, email_to)
    
    with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.login(settings.SMTP_USER, settings.SMTP_PASS)
        server.send_message(msg_content)