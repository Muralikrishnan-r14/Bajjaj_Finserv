from flask import Flask, request, jsonify
import base64
import os

app = Flask(__name__)


# Function to validate and process Base64 files
def handle_file(file_b64):
    if not file_b64:
        return False, "", 0
    try:
        file_data = base64.b64decode(file_b64)
        file_size_kb = len(file_data) / 1024  # Size in KB
        mime_type = "application/octet-stream"  # Default MIME type

        # Detect MIME type (example based on PNG)
        if file_data.startswith(b'\x89PNG'):
            mime_type = "image/png"
        elif file_data.startswith(b'%PDF'):
            mime_type = "application/pdf"

        return True, mime_type, file_size_kb
    except Exception:
        return False, "", 0


# POST route
@app.route('/bfhl', methods=['POST'])
def handle_post():
    data = request.json.get('data', [])
    file_b64 = request.json.get('file_b64', '')

    # Separate numbers and alphabets
    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]

    # Find highest lowercase alphabet
    lowercase_alphabets = [ch for ch in alphabets if ch.islower()]
    highest_lowercase = max(lowercase_alphabets) if lowercase_alphabets else None

    # Handle file processing
    file_valid, file_mime_type, file_size_kb = handle_file(file_b64)

    # Example user information
    user_id = "john_doe_17091999"
    email = "john@xyz.com"
    roll_number = "ABCD123"

    response = {
        "is_success": True,
        "user_id": user_id,
        "email": email,
        "roll_number": roll_number,
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else [],
        "file_valid": file_valid,
        "file_mime_type": file_mime_type,
        "file_size_kb": file_size_kb
    }

    return jsonify(response), 200


# GET route
@app.route('/bfhl', methods=['GET'])
def handle_get():
    response = {
        "operation_code": 1
    }
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(debug=True)
