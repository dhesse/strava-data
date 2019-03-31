import flask
import urllib.parse
import requests
import yaml
from secret import CLIENT_ID, CLIENT_SECRET

app = flask.Flask(__name__)

@app.route('/')
def auth():
    base_url_fmt = 'https://www.strava.com/oauth/authorize?{0}'
    params = {'client_id': CLIENT_ID,
              'redirect_uri': 'http://localhost:5000/auth',
              'response_type': 'code',
              'approval_promt': 'auto',
              'scope': 'activity:read_all'}
    param_string = urllib.parse.urlencode(params)
    return base_url_fmt.format(param_string)

@app.route('/auth')
def receive_auth():
    code = flask.request.args['code']
    token_url = 'https://www.strava.com/oauth/token'
    response = requests.post(token_url, {'client_id': CLIENT_ID,
                                         'client_secret': CLIENT_SECRET,
                                         'code': code,
                                         'grant_type': 'authorization_code'})
    with open('auth.yaml', 'w') as of:
        of.write(yaml.dump(response.json(), default_flow_style=None))
    return 'Authenticated!'