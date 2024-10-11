import requests
import csv

# SonarQube server details
SONAR_HOST = "http://172.31.34.52:9000"
PROJECT_KEY = "my-app"
AUTH_TOKEN = "squ_1c7e965b714e9bb1ed601e6be5ed8d4a2aee94ea"  

# Fetch issues data from SonarQube API
url = f"{SONAR_HOST}/api/issues/search?componentKeys={PROJECT_KEY}&resolved=false"
headers = {"Authorization": f"Basic {AUTH_TOKEN}"}
response = requests.get(url, headers=headers)
data = response.json()

# Write data to CSV file
with open('sonarqube_report.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Issue Key", "Severity", "Type", "Message", "Line"])
    
    for issue in data['issues']:
        writer.writerow([issue['key'], issue['severity'], issue['type'], issue['message'], issue['line']])
