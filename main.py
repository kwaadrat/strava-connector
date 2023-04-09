import requests
import urllib3
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

activites_url = "https://www.strava.com/api/v3/athlete/activities"

access_token = "794fa0f4dbf982dcec1c48358924700849665ba1"

header = {'Authorization': 'Bearer ' + access_token}
param = {'per_page': 1, 'page': 1}
my_dataset = requests.get(activites_url, headers=header, params=param).json()

print(my_dataset)