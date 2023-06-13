import requests

# Set your LinkedIn API credentials
CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret'
ACCESS_TOKEN = 'your_access_token'

def get_employee_info(company_id):
    # Set the endpoint URL for retrieving company employees
    url = f"https://api.linkedin.com/v2/shares?q=owners&owners=urn:li:organization:{company_id}&count=100"

    # Set the authorization header with the access token
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }

    # Send a GET request to the LinkedIn API
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        # Extract employee names and titles from the response
        employees = []
        for element in data["elements"]:
            try:
                name = element["author"]["name"]
                title = element["author"]["jobTitle"]
                employees.append({"name": name, "title": title})
            except KeyError:
                continue

        return employees

    else:
        print("Failed to retrieve employee information from LinkedIn API.")
        return None

# Example usage
company_id = "123456"  # Replace with the actual company ID
employee_info = get_employee_info(company_id)

if employee_info:
    for employee in employee_info:
        print(f"Name: {employee['name']}\tTitle: {employee['title']}")
else:
    print("Failed to fetch employee information from LinkedIn.")
