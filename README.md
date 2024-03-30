# GitHub Webhook Receiver

This repository contains a Flask application for receiving GitHub webhook events and storing them in MongoDB. The application is designed to handle webhook events triggered by GitHub actions such as "Push", "Pull Request", and "Merge".

## Installation

1. Clone this repository to your local machine:
git clone https://github.com/ravinani5689/action-repo.git


2. Install dependencies using pip:

pip install -r requirements.txt

3. Set up a MongoDB instance and configure the connection string in the Flask application.

## Usage

1. Start the Flask application:
python app.py

2. The application will start running on http://localhost:5000/webhook. Update the GitHub repository webhook URL to point to this endpoint.

3. Trigger events such as "Push", "Pull Request", and "Merge" in your GitHub repository to send webhook payloads to the Flask application.

4. Monitor the Flask application logs to verify that it correctly receives and processes the webhook payloads.

## MongoDB Schema

The Flask application stores webhook event data in MongoDB according to the following schema:

{
"action": "string",
"author": "string",
"from_branch": "string",
"to_branch": "string",
"timestamp": "string"
}

