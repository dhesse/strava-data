import requests
import itertools
from secret import CLIENT_ID, CLIENT_SECRET

def get_activities(page, auth):
    headers = {"Authorization": "Bearer {access_token}".format(**auth)}
    params = {'before': None, 'after': None, 'page': page, 'per_page': None}
    url = 'https://www.strava.com/api/v3/athlete/activities'
    return requests.get(url, headers=headers, params=params).json()

def iter_activitiy_pages(auth):
    for i in itertools.count(1):
        page = get_activities(i, auth)
        if page:
            yield page
        else:
            break

def iter_activities(auth):
    for page in iter_activitiy_pages(auth):
        for activity in page:
            yield activity

def refresh_token(auth):
    token_url = 'https://www.strava.com/oauth/token'
    response = requests.post(token_url, {'client_id': CLIENT_ID,
                                         'client_secret': CLIENT_SECRET,
                                         'refresh_token': auth['refresh_token'],
                                         'grant_type': 'refresh_token'})
    return response.json()

def get_activity(id, auth):
    headers = {"Authorization": "Bearer {access_token}".format(**auth)}
    url = 'https://www.strava.com/api/v3/activities/{id}'.format(id=id)
    return requests.get(url,
                        params={'include_all_efforts': True},
                        headers=headers).json()