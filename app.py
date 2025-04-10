from flask import Flask, request, jsonify
from models import db, Episode, Guest, Appearance
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///lateshow.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return {"message": "Late Show API"}

# GET /episodes
@app.route('/episodes')
def get_episodes():
    return jsonify([e.to_dict() for e in Episode.query.all()]), 200

# GET /episodes/:id
@app.route('/episodes/<int:id>')
def get_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({"error": "Episode not found"}), 404
    data = episode.to_dict()
    data["appearances"] = [a.to_dict() for a in episode.appearances]
    return jsonify(data), 200

# GET /guests
@app.route('/guests')
def get_guests():
    return jsonify([g.to_dict() for g in Guest.query.all()]), 200

# POST /appearances
@app.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()
    try:
        new = Appearance(
            rating=data['rating'],
            guest_id=data['guest_id'],
            episode_id=data['episode_id']
        )
        db.session.add(new)
        db.session.commit()
        return jsonify(new.to_dict()), 201
    except Exception as e:
        return jsonify({"errors": [str(e)]}), 400
