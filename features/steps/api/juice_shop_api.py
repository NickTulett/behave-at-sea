import requests

def check_challenge_solved(context, challenge):
    challenge_statuses = requests.request("GET", f"{context.base_url}/api/Challenges/?name={challenge}").json()
    return challenge_statuses["data"][0]["solved"] == True