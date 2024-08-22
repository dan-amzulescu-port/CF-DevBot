import json

def process_dependabot():
    with open('dependabot/dependabot-output.json', 'r') as file:
        alerts = json.load(file)

    vulnerabilities = []

    for alert in alerts:
        vulnerability = {
            "identifier": str(alert['number']),
            "title": f"{alert['dependency']['package']['name']} vulnerability",
            "icon": "Dependabot",
            "properties": {
                "number": alert['number'],
                "state": alert['state'],
                "package_name": alert['dependency']['package']['name'],
                "ecosystem": alert['dependency']['package']['ecosystem'],
                "severity": alert['security_advisory']['severity'],
                "summary": alert['security_advisory']['summary'],
                "description": alert['security_advisory']['description'],
                "cvss_score": alert['security_advisory'].get('cvss', {}).get('score', 0),
                "cwe_id": alert['security_advisory']['cwes'][0]['cwe_id'] if alert['security_advisory']['cwes'] else None,
                "url": alert['html_url'],
                "updated_at": alert['updated_at']
            },
            "relations": {
                "service": "your-repo-name",
                "pull_request": "associated-pr-number"
            }
        }
        vulnerabilities.append(vulnerability)

    with open('dependabot/processed_dependabot.json', 'w') as file:
        json.dump(vulnerabilities, file, indent=2)

if __name__ == "__main__":
    process_dependabot()
