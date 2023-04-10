import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# API url to all activities.

activites_url = "https://www.strava.com/api/v3/athlete/activities"

# Access token.

access_token = "<token>"

# Request.

header = {'Authorization': 'Bearer ' + access_token}
param = {'per_page': 1, 'page': 1}
link = 
my_dataset = requests.get(activites_url, headers=header, params=param).json()

# Print data from API.

print(my_dataset)

# Save data to csv

# my_dataset.to_csv('strava.csv')