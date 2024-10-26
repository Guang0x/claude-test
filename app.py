from flask import Flask, request, jsonify, render_template
from anthropic import Anthropic
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

def get_api_key():
    key = os.getenv("ANTHROPIC_API_KEY")
    # Print first 10 characters of key for debugging (safe to show sk-ant-xxx)
    if key:
        print(f"API key starts with: {key[:10]}...")
    return key

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        api_key = get_api_key()
        if not api_key:
            return jsonify({"error": "API key is not set"}), 401

        # Create a new client instance for each request
        client = Anthropic(
            api_key=api_key.strip()  # Ensure no whitespace
        )

        data = request.json
        user_message = data.get('message', '')

        # Simple test message
        messages = [
            {
                "role": "user",
                "content": user_message
            }
        ]

        try:
            response = client.messages.create(
                model="claude-3-sonnet-20240229",
                messages=messages,
                max_tokens=1024,
                temperature=0.7,
            )
            return jsonify({"response": response.content[0].text})
            
        except Exception as api_error:
            print(f"API Error details: {str(api_error)}")
            return jsonify({"error": f"API Error: {str(api_error)}"}), 401

    except Exception as e:
        print(f"Server Error details: {str(e)}")
        return jsonify({"error": f"Server Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
