from flask import Blueprint, request, jsonify
from app.models import User, Contact
from app import db
from datetime import datetime, date

routes = Blueprint('routes', __name__)

@routes.route('/add_contact', methods=['POST'])
def add_contact():
    data = request.json

    user_phone = data.get('user_phone')
    user_name = data.get('user_name')
    contact_name = data.get('contact_name')
    event_type = data.get('event_type')  # 'birthday' or 'anniversary'
    event_date_str = data.get('event_date')  # Format: YYYY-MM-DD

    # Validate input
    if not all([user_phone, user_name, contact_name, event_type, event_date_str]):
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        event_date = datetime.strptime(event_date_str, '%Y-%m-%d').date()
    except ValueError:
        return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD.'}), 400

    # Check if user exists
    user = User.query.filter_by(phone=user_phone).first()
    if not user:
        user = User(name=user_name, phone=user_phone)
        db.session.add(user)
        db.session.commit()

    # Add contact
    contact = Contact(
        user_id=user.id,
        name=contact_name,
        event_type=event_type.lower(),
        event_date=event_date
    )
    db.session.add(contact)
    db.session.commit()

    return jsonify({'message': 'Contact added successfully'})

@routes.route('/today_reminders', methods=['POST'])
def today_reminders():
    data = request.get_json()
    user_phone = data.get('user_phone')

    if not user_phone:
        return jsonify({'error': 'user_phone is required'}), 400

    user = User.query.filter_by(phone=user_phone).first()
    if not user:
        return jsonify({'error': 'User not found'}), 404

    today = date.today()
    contacts = Contact.query.filter(
        Contact.user_id == user.id,
        db.extract('month', Contact.event_date) == today.month,
        db.extract('day', Contact.event_date) == today.day
    ).all()

    result = [
        {
            'name': contact.name,
            'event_type': contact.event_type,
            'event_date': contact.event_date.strftime('%Y-%m-%d')
        }
        for contact in contacts
    ]

    return jsonify({'today_reminders': result})
