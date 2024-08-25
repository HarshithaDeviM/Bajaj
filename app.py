from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/bfhl', methods=['POST'])
def process_post():
    data = request.json.get("data", [])
    user_id = "Markapuram_Harshitha_Devi_09092004"
    email = "harshitha.21bce7088@vitapstudent.ac.in"
    roll_number = "21BCE7088"
    
    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]
    lower_case_alphabets = [item for item in alphabets if item.islower()]
    highest_lowercase_alphabet = max(lower_case_alphabets) if lower_case_alphabets else None
    
    response = {
        "is_success": True,
        "user_id": user_id,
        "email": email,
        "roll_number": roll_number,
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
    }
    return jsonify(response)

@app.route('/bfhl', methods=['GET'])
def process_get():
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(debug=True)
