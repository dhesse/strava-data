import requests
import itertools

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