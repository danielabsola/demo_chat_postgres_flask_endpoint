from flask import Flask
from flask_cors import CORS
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.resolve()))
# Routes
from routes import chat_history_companion
# Config
from config import config


app=Flask(__name__)

CORS(app, resources={"*":{"origins":["http://localhost:9300", "http://example.com"]}})

def page_not_found(error):
    return "<h1>Not found page<h1/>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    #Blueprints
    app.register_blueprint(chat_history_companion.main, url_prefix='/api/companion')
    # Error handlers
    app.register_error_handler(404, page_not_found)
    app.run()