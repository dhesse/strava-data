# Strava Data Getter

Minimal example around getting some of your data for analysis from Strava.

# Usage

1. Clone this repository.
2. Create your `secret.py` from the [template](secret.py.template).
3. Run the [server](server.py), like so:
       FLASK_APP=server.py flask run
4. Open the link you find at [http://localhost:5000/](http://localhost:5000)
5. Start [jupyter lab](https://jupyterlab.readthedocs.io/en/stable/) and open [GetActivities.ipynb](GetActivities.ipynb).