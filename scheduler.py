from app import create_app, db
from app.models import User
from remainder import get_today_reminders
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

def send_daily_reminders():
    with app.app_context():
        users = User.query.all()
        for user in users:
            msg = get_today_reminders(user.phone)
            if msg:
                print(f"[{datetime.now()}] To {user.phone}: {msg}")  # Replace this with WhatsApp later

app = create_app()
scheduler = BackgroundScheduler()
scheduler.add_job(func=send_daily_reminders, trigger='cron', hour=14, minute=51)
scheduler.start()
