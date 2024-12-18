from email.message import EmailMessage
from app.config import settings


from pydantic import EmailStr

def create_booking_confirmation_template(
    rent: dict,
    good: dict,
    email_to: EmailStr
):
    email = EmailMessage()
    
    email["Subject"] = "Подтверждение аренды"
    email["From"] = settings.SMTP_USER
    email["To"] = email_to
    
    
    email.set_content(
        f"""
            <h1>Подтверждение аренды</h1>
            Вы арендуете {good["name"]} на срок с {rent["date_from"]} по {rent["date_to"]} с ежедневной
            оплатой {good["price_per_day"]}. Приятного пользования!
        """,
        subtype="html"
    )
    
    return email