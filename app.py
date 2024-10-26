from flask import Flask, request, jsonify, render_template
from marie.response import MarieResponseGenerator
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Initialize Marie
marie = MarieResponseGenerator()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message')
        
        # Get Marie's response
        response = marie.generate_response(user_message)
        
        return jsonify({
            "response": response,
            "status": "success"
        })
        
    except Exception as e:
        print(f"Error in /api/chat: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)