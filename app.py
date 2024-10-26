from flask import Flask, request, jsonify, render_template
from anthropic import Anthropic
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

def check_api_key():
    key = os.getenv("ANTHROPIC_API_KEY")
    if not key:
        return "API key is missing"
    if not key.startswith("sk-ant"):
        return "API key format is incorrect"
    return "API key looks valid"

@app.route('/')
def home():
    api_status = check_api_key()
    return render_template('index.html', api_status=api_status)

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        # Check API key before making the request
        api_status = check_api_key()
        if "invalid" in api_status or "missing" in api_status:
            return jsonify({"error": f"API Key Error: {api_status}"}), 401

        # Initialize Anthropic client for each request
        anthropic = Anthropic(
            api_key=os.getenv("ANTHROPIC_API_KEY")
        )

        data = request.json
        user_message = data.get('message')
        
        # Make a simple test request
        response = anthropic.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=1024,
            messages=[{
                "role": "user",
                "content": user_message
            }]
        )
        
        return jsonify({
            "response": response.content[0].text,
        })
        
    except Exception as e:
        print(f"Error in /api/chat: {str(e)}")  # Server-side logging
        return jsonify({
            "error": f"Error: {str(e)}",
            "api_status": check_api_key()
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
