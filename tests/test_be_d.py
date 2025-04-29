import pytest
from ..test_d import app, letters_db, custom_shuffle, validate_username
import json
from datetime import datetime

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_validate_username():
    # Test username validation
    assert validate_username("abacca") == True
    assert validate_username("Cabbie") == False  # no 'c' after 'ab'
    assert validate_username("Acaiberrycake") == True

def test_login_success(client):
    # Test successful login
    response = client.post('/api/login', 
                         json={'username': 'abacca', 'password': 'accaba'})
    assert response.status_code == 200
    assert b'Login successful' in response.data

def test_login_invalid_username(client):
    # Test invalid username
    response = client.post('/api/login', 
                         json={'username': 'Cabbie', 'password': 'eibbaC'})
    assert response.status_code == 401
    assert b'Invalid username' in response.data

def test_login_invalid_password(client):
    # Test invalid password
    response = client.post('/api/login', 
                         json={'username': 'abacca', 'password': 'wrong'})
    assert response.status_code == 401
    assert b'Invalid password' in response.data

def test_list_letters(client):
    # Test listing letters
    response = client.get('/api/letters')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['letters'] == ['A', 'B']

def test_get_letter_(client):
    # Test getting a specific letter for A & B
    response_a = client.get('/api/letter/A')
    response_b = client.get('/api/letter/B')
    assert response_a.status_code == 200
    assert response_b.status_code == 200
    data_a = json.loads(response_a.data)
    data_b = json.loads(response_b.data)
    assert data_a == {'letter': 'A', 'value': 1, 'strokes': 2, 'vowel': True}
    assert data_b == {'letter': 'B', 'value': 2, 'strokes': 1, 'vowel': False}
    
def test_get_nonexistent_letter(client):
    # Test getting a letter that doesn't exist
    response = client.get('/api/letter/X')
    assert response.status_code == 404

def test_add_letter_success(client):
    # Test successfully adding a new letter
    response = client.post('/api/letter/add', 
                         json={'letter': 'C', 'value': 3, 'strokes': 2, 'vowel': False})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 0

    # Verify the letter was added
    response = client.get('/api/letter/C')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['letter'] == 'C'

def test_add_duplicate_letter(client):
    # Test adding a duplicate letter
    response = client.post('/api/letter/add', 
                         json={'letter': 'A', 'value': 1, 'strokes': 2, 'vowel': True})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 1

def test_add_letter_invalid_data(client):
    # Test adding a letter with invalid data
    # Missing required field
    response = client.post('/api/letter/add', 
                         json={'letter': 'D', 'value': 4, 'strokes': 3})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 1

    # Strokes equals value
    response = client.post('/api/letter/add', 
                         json={'letter': 'D', 'value': 4, 'strokes': 4, 'vowel': False})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 1

def test_shuffle_letters(client):
    # Test shuffling letters (we can't test randomness, but we can test structure)
    response = client.get('/api/letter/shuffle')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data['letters']) == len(letters_db)
    assert set(data['letters']) == set(letters_db.keys())

def test_custom_shuffle():
    # Test our custom shuffle function
    items = [1, 2, 3, 4, 5]
    shuffled = custom_shuffle(items)
    assert len(shuffled) == len(items)
    assert set(shuffled) == set(items)
    # Note: There's a very small chance this could fail if shuffle returns original order
    assert shuffled != items or shuffled != sorted(items)

def test_filter_letters(client):
    # Test filtering letters by value
    response = client.get('/api/letter/filter/1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['letters'] == ['A']

    # Add a new letter and test again
    client.post('/api/letter/add', 
              json={'letter': 'D', 'value': 1, 'strokes': 3, 'vowel': False})
    response = client.get('/api/letter/filter/1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['letters'] == ['A', 'D']