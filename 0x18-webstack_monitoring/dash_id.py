import requests
import json

# Define your Datadog API and Application Keys
DD_API_KEY = "9ff7af27243dc94b2f5b1e0e4d0584e3"
DD_APP_KEY = "187e1fab43ad1b02d26e27288760d7e15567c26e"

# Define the URL for the Datadog API
url = "https://api.datadoghq.com/api/v1/dashboard"

# Set the headers for the API request
headers = {
    "DD-API-KEY": DD_API_KEY,
    "DD-APPLICATION-KEY": DD_APP_KEY
}

# Make the API request to fetch all dashboards
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    dashboards = response.json()
    
    # Debug: Print the API response
    print("API Response:")
    print(json.dumps(dashboards, indent=2))

    # Find the dashboard named "william" and extract its id
    dashboard_id = None
    for dashboard in dashboards.get('dashboards', []):
        if dashboard.get('title') == "william":
            dashboard_id = dashboard.get('id')
            break

    # Check if the dashboard_id was found
    if dashboard_id:
        # Create the answer file with the dashboard_id
        with open("2-setup_datadog", "w") as f:
            f.write(dashboard_id)
        print("Dashboard ID has been written to 2-setup_datadog")
    else:
        print("Dashboard named 'william' not found")
else:
    print(f"Failed to fetch dashboards. Status code: {response.status_code}")
    print("Response:", response.text)

