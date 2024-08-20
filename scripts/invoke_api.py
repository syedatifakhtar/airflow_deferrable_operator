import requests
from requests.auth import HTTPBasicAuth

# Define the API endpoint
api_url = "https://your-api-endpoint.com/your-api-path"  # Replace with your API endpoint

# Optional headers (if required by the API)
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_ACCESS_TOKEN"  # Replace with your access token if needed
}

# Function to make the API call
def invoke_api(number):
    try:
        airflow_url = f"http://localhost:8080/api/v1/dags/loop_atifs_dag{number}/dagRuns"
        # Replace with your Airflow credentials
        username = "airflow"
        password = "airflow"

        # Payload to trigger the DAG
        payload = {
            "conf": {}  # You can pass additional configuration parameters if your DAG expects them
        }
        # Make the POST request to trigger the DAG
        response = requests.post(
            airflow_url,
            json=payload,
            auth=HTTPBasicAuth(username, password)  # Use HTTPBasicAuth for authentication
        )

        # Check the response
        if response.status_code == 200:
            print("DAG triggered successfully!")
            print("Response:", response.json())
        else:
            print(f"Failed to trigger DAG. Status code: {response.status_code}")
            print("Response:", response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

# Invoke the API 100 times
for i in range(1000):
    print(f"Invoking API call {i + 1} of 100...")
    invoke_api(i)
