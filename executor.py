import requests

def execute_code(code, language='python3'):
    # Replace with your API credentials
    client_id = 'YOUR_CLIENT_ID'
    client_secret = 'YOUR_CLIENT_SECRET'
    url = 'https://api.jdoodle.com/v1/execute'

    language_mapping = {
        'python': 'python3',
        'javascript': 'nodejs',
        'ruby': 'ruby'
    }

    language_api = language_mapping.get(language, 'python3')

    headers = {
        'Content-Type': 'application/json',
    }

    data = {
        'clientId': client_id,
        'clientSecret': client_secret,
        'script': code,
        'language': language_api,
        'versionIndex': '3' if language_api == 'python3' else '0'
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()
