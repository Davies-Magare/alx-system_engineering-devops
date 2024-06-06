#!/usr/bin/python3

"""
Retrieve the user metrics of a given subreddit
"""

import json
import requests
import sys


def number_of_subscribers(subreddit):
    """Return the number of subscribers of a given subreddit"""

    app_id = 'b-pGh9ktJwVslAVVrwsW7A'
    secret_key = 'Vm6PQTUYOj3G1LOhZ4mO05fGX4ILvQ'
    auth = requests.auth.HTTPBasicAuth(app_id, secret_key)
    username = 'Dry-Birthday8239'
    password = 'Biochemist79'
    data = {
            'grant_type': 'password',
            'username': username,
            'password': password
    }
    headers = {'User-Agent': 'ApiProject/001'}
    result = requests.post('https://www.reddit.com/api/v1/access_token',
                           auth=auth, data=data, headers=headers)

    access_token = result.json()['access_token']

    headers.update({"Authorization": f"bearer {access_token}"})
    response = requests.get('https://oauth.reddit.com/r/{}/about'
                            .format(sys.argv[1]), headers=headers)

    if 'subscribers' in response.json()['data']:
        return response.json()['data']['subscribers']
    return 0
