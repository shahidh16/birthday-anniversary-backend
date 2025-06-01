from datetime import date
from app import db
from app.models import User, Contact

def get_today_reminders(user_phone):
    user = User.query.filter_by(phone=user_phone).first()
    if not user:
        return None

    today = date.today()
    contacts = Contact.query.filter(
        Contact.user_id == user.id,
        db.extract('month', Contact.event_date) == today.month,
        db.extract('day', Contact.event_date) == today.day
    ).all()

    if not contacts:
        return None

    messages = []
    for c in contacts:
        messages.append(f"{c.name}'s {c.event_type} is today ({c.event_date.strftime('%Y-%m-%d')}).")

    reminder_message = "\n".join(messages)
    return reminder_message