from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)

### === Swagger UI Setup === ###
SWAGGER_URL = '/docs'  # URL to access Swagger UI
API_URL = '/static/swagger.json'  # This is where your swagger.json actually is

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "AI API Wrapper"}
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

### === Sample API Endpoint === ###
@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()

    if not data or 'prompt' not in data:
        return jsonify({'error': 'Missing "prompt" in request body'}), 400

    prompt = data['prompt']
    response = f"Simulated AI response to: {prompt}"

    return jsonify({
        'prompt': prompt,
        'response': response
    })

if __name__ == '__main__':
    app.run(debug=True)
