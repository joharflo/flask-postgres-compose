from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv


app = Flask(__name__)

# Configure the PostgreSQL connection
sever_db=os.getenv('SERVER_NAME_DB')
user= os.getenv('POSTGRES_USER')
password=os.getenv('POSTGRES_PASSWORD')
db=os.getenv('POSTGRES_DB')

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{sever_db}/{db}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the model matching the existing table
class Item(db.Model):
    __tablename__ = 'items'  # Make sure this matches the existing table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=True)

# Route to get all items
@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([{'id': item.id, 'name': item.name, 'description': item.description} for item in items])

# Route to get a single item by ID
@app.route('/items/<int:id>', methods=['GET'])
def get_item(id):
    item = Item.query.get_or_404(id)
    return jsonify({'id': item.id, 'name': item.name, 'description': item.description})

# Route to create a new item
@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    new_item = Item(name=data['name'], description=data.get('description'))
    db.session.add(new_item)
    db.session.commit()
    return jsonify({'id': new_item.id, 'name': new_item.name, 'description': new_item.description}), 201

# Route to update an existing item
@app.route('/items/<int:id>', methods=['PUT'])
def update_item(id):
    data = request.get_json()
    item = Item.query.get_or_404(id)
    item.name = data['name']
    item.description = data.get('description')
    db.session.commit()
    return jsonify({'id': item.id, 'name': item.name, 'description': item.description})

# Route to delete an item
@app.route('/items/<int:id>', methods=['DELETE'])
def delete_item(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'Item deleted'})

if __name__ == '__main__':
    app.run(debug=True)
