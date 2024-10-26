from flask import Flask, request, jsonify, render_template
from anthropic import Anthropic
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Print API key status (will only show if key exists, not the actual key)
api_key = os.getenv("ANTHROPIC_API_KEY")
print(f"API Key exists: {bool(api_key)}")
print(f"API Key starts with: {api_key[:8] if api_key else 'None'}")

anthropic = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# Store conversations in memory (for demonstration)
conversations = {}

@app.route('/')
def home():
    # Add API key status to template
    api_status = bool(os.getenv("ANTHROPIC_API_KEY"))
    return render_template('index.html', api_status=api_status)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    conversation_id = data.get('conversation_id', 'default')
    
    # Debug print
    print(f"Attempting to use API key starting with: {os.getenv('ANTHROPIC_API_KEY')[:8] if os.getenv('ANTHROPIC_API_KEY') else 'None'}")
    
    # Initialize conversation history if it doesn't exist
    if conversation_id not in conversations:
        conversations[conversation_id] = []
    
    # Add user message to history
    conversations[conversation_id].append({
        "role": "user",
        "content": user_message
    })
    
    try:
        # Get response from Claude
        response = anthropic.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=1024,
            messages=conversations[conversation_id]
        )
        
        # Add assistant's response to history
        assistant_message = response.content[0].text
        conversations[conversation_id].append({
            "role": "assistant",
            "content": assistant_message
        })
        
        return jsonify({
            "response": assistant_message,
            "conversation_id": conversation_id
        })
        
    except Exception as e:
        print(f"Error details: {str(e)}")  # Debug print
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
