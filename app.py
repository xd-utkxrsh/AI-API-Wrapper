from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from dotenv import load_dotenv
import os
import openai

# Load environment variables
load_dotenv()

# Set OpenAI API key (fallback to empty string if not set)
openai.api_key = os.getenv("OPENAI_API_KEY", "")

app = Flask(__name__)
CORS(app)

# === Swagger UI Setup ===
SWAGGER_URL = '/docs'
API_URL = '/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "AI API Wrapper"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# === /generate Endpoint ===
@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()

    if not data or 'prompt' not in data:
        return jsonify({'error': 'Missing "prompt" in request body'}), 400

    prompt = data['prompt']
    model = data.get('model', 'gpt-3.5-turbo')

    # Simulated/fallback response if API key is missing or blank
    if not openai.api_key:
        fake_response = f"(Simulated GPT response) You said: {prompt}"
        return jsonify({'prompt': prompt, 'response': fake_response})

    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        return jsonify({
            'prompt': prompt,
            'response': response.choices[0].message['content']
        })

    except Exception as e:
    #  Fallback to mock response
        return jsonify({
            'prompt': prompt,
            'response': "This is a mock GPT response for testing purposes.",  # ✅ Show mock output here
            'error': f"(Fallback) Could not generate GPT response. Error: {str(e)}"
        }), 200


if __name__ == '__main__':
    app.run(debug=True)
