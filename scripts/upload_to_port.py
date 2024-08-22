import os
import requests
import json

# Read the processed data
with open('processed_data.json') as f:
    data = json.load(f)

# Port API URL and Authentication
api_url = 'https://api.getport.io/v1/blueprints/dependabot/entities'
api_key = os.getenv('PORT_API_KEY')

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
}

# Upload data to Port
for entity in data['entities']:
    response = requests.post(api_url, headers=headers, json=entity)
    if response.status_code == 201:
        print(f"Successfully created entity: {entity['identifier']}")
    else:
        print(f"Failed to create entity: {response.text}")
