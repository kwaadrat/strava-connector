import json
import os
import requests
import time

# Initial Settings
client_id = '93013'
client_secret = '54eee8b78fcf488ed36e3f8c50a0165a375ed4f6'
redirect_uri = 'http://localhost/'


def refreshToken()

        # Authorization URL
    request_url = f'http://www.strava.com/oauth/authorize?client_id={client_id}' \
                    f'&response_type=code&redirect_uri={redirect_uri}' \
                    f'&approval_prompt=force' \
                    f'&scope=profile:read_all,activity:read_all'

        # User prompt showing the Authorization URL
        # and asks for the code
    print('Click here:', request_url)
    print('Please authorize the app and copy&paste below the generated code!')
    print('P.S: you can find the code in the URL')
    code = input('Insert the code from the url: ')

    # Get the access token
    token = requests.post(url='https://www.strava.com/api/v3/oauth/token',
                       data={'client_id': client_id,
                             'client_secret': client_secret,
                             'code': code,
                             'grant_type': 'authorization_code'})

#Save json response as a variable
    strava_token = token.json()

    with open('strava_token.json', 'w') as outfile:
        json.dump(strava_token, outfile)


# GET ATHLETE INFO


# Read the token from the saved file
with open('strava_token.json', 'r') as token:
  data = json.load(token)

# Get the access token
access_token = data['access_token']

# Build the API url to get athlete info
athlete_url = f"https://www.strava.com/api/v3/athlete?" \
              f"access_token={access_token}"

# Get the response in json format
response = requests.get(athlete_url)
athlete = response.json()

# Print out the retrieved information
print('RESTful API:', athlete_url)
print('='* 5, 'ATHLETE INFO', '=' * 5)
print('Name:', athlete['firstname'], '"' + athlete['username'] + '"', athlete['lastname'])
print('Gender:', athlete['sex'])
print('City:', athlete['city'], athlete['country'])
print('Strava athlete from:', athlete['created_at'])

# Read the token from the saved file
with open('strava_token.json', 'r') as token:
  data = json.load(token)

# Build the API url to get activities data
activities_url = f"https://www.strava.com/api/v3/athlete/activities?" \
          f"access_token={access_token}"
print('RESTful API:', activities_url)

# Get the response in json format
response = requests.get(activities_url)
activity = response.json()[5]

# Print out the retrieved information
print('='*5, 'SINGLE ACTIVITY', '='*5)
print('Athlete:', athlete['firstname'], athlete['lastname'])
print('Name:', activity['name'])
print('Date:', activity['start_date'])
print('Disance:', activity['distance'], 'm')
print('Average Speed:', activity['average_speed'], 'm/s')
print('Max speed:', activity['max_speed'], 'm/s')
print('Moving time:', round(activity['moving_time'] / 60, 2), 'minutes')
print('Location:', activity['location_city'], 
      activity['location_state'], activity['location_country'])