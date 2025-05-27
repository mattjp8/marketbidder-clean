from flask_sqlalchemy import SQLAlchemy
import os
from flask import Flask, jsonify
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
class RFQ(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    deadline = db.Column(db.String(40), nullable=False)



app = Flask(__name__)

@app.route('/')
def home():
    return "✅ MarketBidder API is live!"

@app.route('/api/rfqs')
def get_rfqs():
    rfqs = RFQ.query.all()
    return jsonify([{
        'id': rfq.id,
        'title': rfq.title,
        'description': rfq.description,
        'deadline': rfq.deadline
    } for rfq in rfqs])

@app.route('/api/rfqs', methods=['POST'])
def create_rfq():
    data = request.json
    new_rfq = RFQ(
        title=data['title'],
        description=data['description'],
        deadline=data['deadline']
    )
    db.session.add(new_rfq)
    db.session.commit()
    return jsonify({'message': 'RFQ created', 'id': new_rfq.id}), 201


with app.app_context():
    db.create_all()
