import json


def process_dependabot():
    with open('dependabot/dependabot-output.json') as f:
        data = json.load(f)

    vulnerabilities = []
    for alert in data:
        vulnerabilities.append({
            "identifier": alert['id'],
            "title": alert['title'],
            "description": alert['description'],
            "severity": alert['severity'],
            "package": alert['package'],
            "version": alert['version'],
            "fixed_version": alert['fixed_version'],
            "repo": alert['repo'],
            "pr": alert['pr']
        })

    with open('dependabot/processed_data.json', 'w') as f:
        json.dump(vulnerabilities, f)


if __name__ == "__main__":
    process_dependabot()
