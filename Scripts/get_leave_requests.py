import requests
import json

# SharePoint site and list details
sharepoint_site = 'https://yourcompany.sharepoint.com/sites/YourSite'
list_name = 'LeaveRequests'
access_token = 'YOUR_ACCESS_TOKEN'

# Function to get leave requests from SharePoint
def get_leave_requests():
    url = f"{sharepoint_site}/_api/web/lists/getbytitle('{list_name}')/items"
    headers = {
        'Accept': 'application/json;odata=verbose',
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        leave_requests = response.json()['d']['results']
        return leave_requests
    else:
        print(f"Error: {response.status_code}")
        return None

if __name__ == "__main__":
    leave_requests = get_leave_requests()
    if leave_requests:
        with open('leave_requests.json', 'w') as file:
            json.dump(leave_requests, file, indent=4)
        print("Leave requests data saved to leave_requests.json")
