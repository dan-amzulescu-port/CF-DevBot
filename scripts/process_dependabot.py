import json


def process_dependabot():
    with open('dependabot/dependabot-output.json', 'r') as f:
        data = json.load(f)

    # Print out the data to see its structure
    print("Raw Data:", data)

    # Assuming data is a list of alerts
    alerts = []

    for alert in data:
        print("Processing Alert:", alert)  # Debug print
        alerts.append({
            "identifier": alert['id'],
            "title": alert['security_advisory']['summary'],
            "severity": alert['security_advisory']['severity'],
            "ecosystem": alert['security_advisory']['ecosystem'],
            "package": alert['security_advisory']['package'],
            "fixed_in": alert['security_advisory']['fixed_in'],
            "repository": alert['repository']['full_name']
        })

    with open('dependabot/processed-dependabot.json', 'w') as f:
        json.dump(alerts, f, indent=2)


if __name__ == "__main__":
    process_dependabot()
