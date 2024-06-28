import requests

# SharePoint site and list details
sharepoint_site = 'https://yourcompany.sharepoint.com/sites/YourSite'
list_name = 'LeaveRequests'
access_token = 'YOUR_ACCESS_TOKEN'

# Function to update leave request status in SharePoint
def update_leave_status(item_id, status, manager_comments=''):
    url = f"{sharepoint_site}/_api/web/lists/getbytitle('{list_name}')/items({item_id})"
    headers = {
        'Accept': 'application/json;odata=verbose',
        'Content-Type': 'application/json;odata=verbose',
        'Authorization': f'Bearer {access_token}',
        'X-HTTP-Method': 'MERGE',
        'IF-MATCH': '*'
    }
    data = {
        '__metadata': {'type': 'SP.Data.LeaveRequestsListItem'},
        'Status': status,
        'ManagerComments': manager_comments
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 204:
        print("Leave request status updated successfully.")
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    item_id = 1  # Example item ID
    status = 'Approved'
    manager_comments = 'Approved by manager.'
    update_leave_status(item_id, status, manager_comments)
