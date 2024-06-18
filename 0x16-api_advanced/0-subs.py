#!/usr/bin/python3

"""
Find the number of users in a subreddit
"""
import json
import requests
import sys


def number_of_subscribers(subreddit):
    """Retrieve the number of subscribers of subreddit"""

    CLIENT_ID = "b-pGh9ktJwVslAVVrwsW7A"
    SECRET_KEY = "Vm6PQTUYOj3G1LOhZ4mO05fGX4ILvQ"

    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)
    data = {
            'grant_type': 'password',
            'username': 'Dry-Birthday8239',
            'password': 'Biochemist79'
    }
    headers = {'User-Agent': 'MyAPI/0.01'}

    res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=auth, data=data, headers=headers)
    TOKEN = res.json()['access_token']
    headers = {**headers, **{'Authorization': f'bearer {TOKEN}'}}
    subreddit_info = requests.get('https://oauth.reddit.com/r/{}/about'
                                  .format(sys.argv[1]), headers=headers,
                                  allow_redirects=False)
    if subreddit_info.status_code == 200:
        return (subreddit_info.json()['data']['subscribers'])
    return 0
