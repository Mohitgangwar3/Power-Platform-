import pandas as pd

# Load leave requests data
leave_requests = pd.read_json('leave_requests.json')

# Analyze data (example: calculate total leave days for each employee)
leave_requests['LeaveStartDate'] = pd.to_datetime(leave_requests['LeaveStartDate'])
leave_requests['LeaveEndDate'] = pd.to_datetime(leave_requests['LeaveEndDate'])
leave_requests['LeaveDays'] = (leave_requests['LeaveEndDate'] - leave_requests['LeaveStartDate']).dt.days + 1

total_leave_days = leave_requests.groupby('EmployeeName')['LeaveDays'].sum().reset_index()

# Save analysis results
total_leave_days.to_csv('total_leave_days.csv', index=False)
print("Total leave days data saved to total_leave_days.csv")
