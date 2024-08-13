#!/usr/bin/python3
import json, requests

def number_of_subscribers(subreddit):
    """
    Get Reddit api authentication and query the number of 
    subscribers of a given subreddit"""
    
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
    response = requests.get(f'https://oauth.reddit.com/r/{subreddit}/about', 
                            headers=headers, allow_redirects=False)
    
    #print(json.dumps(response.json(), indent=4))

    if response.status_code == 200:
        return response.json()['data']['subscribers']
    return 0
    #number_of_subscribers('programming')
