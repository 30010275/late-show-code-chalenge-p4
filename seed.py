from app import app
from models import db, Episode, Guest, Appearance

with app.app_context():
    # Clear existing data
    db.session.query(Appearance).delete()
    db.session.query(Episode).delete()
    db.session.query(Guest).delete()

    # Add episodes
    episodes = [
        Episode(date="1/11/99", number=1),
        Episode(date="1/12/99", number=2),
        Episode(date="1/13/99", number=3)
    ]

    # Add guests
    guests = [
        Guest(name="Michael J. Fox", occupation="actor"),
        Guest(name="Tom Hanks", occupation="actor"),
        Guest(name="Oprah Winfrey", occupation="talk show host")
    ]

    db.session.add_all(episodes + guests)
    db.session.commit()
    print("Database seeded with 3 episodes and 3 guests.")
