from flask import Flask, request, jsonify
from chatbot_engine import generate_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS so frontend can call this

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')
    response = generate_response(user_message)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
