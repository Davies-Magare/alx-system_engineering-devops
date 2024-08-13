#!/usr/bin/python3

"""
Query the reddit API
"""

import json
import requests


def top_ten(subreddit):
    """Print titles of top 10 hot posts"""

    client_id = "Ze7ucSghCV5LdlCn5RgbTw"
    secret_key = "R8ti_aHeU_Ag1CgAiauLTwPcsdv5fg"
    username = "Ashamed_Community_29"
    password = "Biochemist79"
    auth = requests.auth.HTTPBasicAuth(client_id, secret_key)

    data = {
        'grant_type': 'password',
        'username': username,
        'password': password
    }
    headers = {'User-Agent': 'MyAPI-0.0.1'}

    result = requests.post('https://www.reddit.com/api/v1/access_token',
                           auth=auth, data=data, headers=headers)
    token = result.json()['access_token']
    headers['Authorization'] = f'bearer {token}'
    params={'limit': 10}
    response = requests.get(f'https://oauth.reddit.com/r/{subreddit}/hot',
                            headers=headers, allow_redirects=False, params=params)
    if response.status_code == 200:
        #print(json.dumps(response.json(), indent=4))
        for child in response.json()['data']['children']:
            print(child['data']['title'])
    else:
        print("None")
