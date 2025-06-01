from app import create_app, db
from remainder import get_today_reminders

app = create_app()

with app.app_context():
    msg = get_today_reminders("9790306178")
    if msg:
        print("Reminder:\n", msg)
    else:
        print("No reminders today.")
