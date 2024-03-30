from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['webhook_db']

@app.route('/webhook', methods=['POST'])
def webhook():
    payload = request.json
    # Extract relevant data from the payload
    action = payload.get('action')
    author = payload.get('author')
    from_branch = payload.get('from_branch')
    to_branch = payload.get('to_branch')
    timestamp = payload.get('timestamp')
    # Store data in MongoDB
    db.events.insert_one({
        'action': action,
        'author': author,
        'from_branch': from_branch,
        'to_branch': to_branch,
        'timestamp': timestamp
    })
    return 'Webhook received successfully!', 200

if __name__ == '__main__':
    app.run(debug=True)
