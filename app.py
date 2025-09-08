
import os
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

# For production, you should restrict origins like this example:
# CORS(app, resources={r"/*": {"origins": ["http://localhost:3000", "https://your-frontend-domain.com"]}})

# For now, allow all origins for development
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 80))
    app.run(host='0.0.0.0', port=port)
