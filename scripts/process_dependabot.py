import json
import requests
import os

PORT_API_KEY = os.getenv('PORT_API_KEY')


def upload_to_port(entity):
    url = "https://api.getport.io/v1/blueprints/dependabot/entities"
    headers = {
        "Authorization": f"Bearer {PORT_API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, json=entity)
    response.raise_for_status()


def process_dependabot():
    with open('dependabot/dependabot-output.json') as f:
        alerts = json.load(f)

        for alert in alerts:
            entity = {
                "identifier": str(alert['number']),
                "title": alert['security_advisory']['summary'],
                "properties": {
                    "state": alert['state'],
                    "package_name": alert['dependency']['package']['name'],
                    "severity": alert['security_advisory']['severity'],
                    "cve_id": alert['security_advisory']['cve_id'],
                    "ghsa_id": alert['security_advisory']['ghsa_id'],
                    "url": alert['html_url'],
                    "ecosystem": alert['dependency']['package']['ecosystem'],
                    "manifest_path": alert['dependency']['manifest_path']
                },
                "relations": {
                    "service": {
                        "target": "CF-DevBot",  # Replace with actual service identifier
                        "required": True
                    }
                }
            }
            print(json.dumps(entity, indent=2))  # Print the entity before uploading
            upload_to_port(entity)


if __name__ == "__main__":
    process_dependabot()
