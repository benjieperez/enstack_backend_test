from flask import Flask, request, jsonify
import random
from datetime import datetime

app = Flask(__name__)

# In-memory database
letters_db = {
    'A': {'letter': 'A', 'value': 1, 'strokes': 2, 'vowel': True},
    'B': {'letter': 'B', 'value': 2, 'strokes': 1, 'vowel': False}
}

# Custom shuffle function
def custom_shuffle(items):
    # Fisher-Yates shuffle algorithm
    shuffled = list(items)
    for i in range(len(shuffled)-1, 0, -1):
        j = random.randint(0, i)
        shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
    return shuffled

# Helper function to validate username
def validate_username(username):
    username_lower = username.lower()
    if len(username_lower) < 4:
        return False
    
    # Check for 'a', 'b', 'c' in order
    a_index = username_lower.find('a')
    if a_index == -1:
        return False
    
    b_index = username_lower.find('b', a_index)
    if b_index == -1:
        return False
    
    c_index = username_lower.find('c', b_index)
    if c_index == -1:
        return False
    
    return True

# Login endpoint
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username', '')
    password = data.get('password', '')
    
    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400
    
    if not validate_username(username):
        return jsonify({'error': 'Invalid username'}), 401
    
    if password.lower() != username[::-1].lower():
        return jsonify({'error': 'Invalid password'}), 401
    
    return jsonify({'message': 'Login successful'}), 200

# List letters endpoint
@app.route('/api/letters', methods=['GET'])
def list_letters():
    # Get all letters, sorted by value
    sorted_letters = sorted(letters_db.values(), key=lambda x: x['value'])
    letters_list = [letter['letter'] for letter in sorted_letters]
    return jsonify({'letters': letters_list})

# Add letter endpoint
@app.route('/api/letter/add', methods=['POST'])
def add_letter():
    data = request.get_json()
    
    if not data or 'letter' not in data:
        return jsonify({'status': 1})
    
    letter = data['letter']
    
    # Check if letter already exists
    if letter in letters_db:
        return jsonify({'status': 1})
    
    # Validate required fields
    required_fields = ['value', 'strokes', 'vowel']
    for field in required_fields:
        if field not in data:
            return jsonify({'status': 1})
    
    # Check strokes != value
    if data['strokes'] == data['value']:
        return jsonify({'status': 1})
    
    # Add to database
    letters_db[letter] = {
        'letter': letter,
        'value': data['value'],
        'strokes': data['strokes'],
        'vowel': data['vowel']
    }
    
    return jsonify({'status': 0})

# Get letter endpoint
@app.route('/api/letter/<string:letter>', methods=['GET'])
def get_letter(letter):
    if letter not in letters_db:
        return jsonify({'error': 'Letter not found'}), 404
    
    # Return all fields except added_at
    letter_data = letters_db[letter].copy()
    return jsonify(letter_data)

# Shuffle letters endpoint
@app.route('/api/letter/shuffle', methods=['GET'])
def shuffle_letters():
    letters = list(letters_db.keys())
    shuffled = custom_shuffle(letters)
    return jsonify({'letters': ''.join(shuffled)})

# Filter letters endpoint
@app.route('/api/letter/filter/<int:val>', methods=['GET'])
def filter_letters(val):
    filtered = []
    for letter in letters_db.values():
        if letter['value'] <= val:
            filtered.append(letter['letter'])
    return jsonify({'letters': filtered})

if __name__ == '__main__':
    app.run(debug=True)