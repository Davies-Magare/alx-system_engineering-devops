#!/usr/bin/python3
"""
Request for data from an API and wrte it to file in json.
"""


import csv
import json
import requests
import sys


def to_json():
    """Write data to json file."""

    response = requests.get("https://jsonplaceholder.typicode.com/todos",
                            params={"userId": sys.argv[1]})
    response_name = requests.get("https://jsonplaceholder.typicode.com/users",
                                 params={"id": sys.argv[1]})
    dicts = response.json()
    name_dict = response_name.json()
    name = name_dict[0].get('username')
    comp = [[a_dict.get('title'),
             a_dict.get('completed'), name] for a_dict in dicts]
    keys = ['task', 'completed', 'username']

    rows = []
    for lst in comp:
        row = {key: value for key, value in zip(keys, lst)}
        rows.append(row)
    filename = "{}.json".format(sys.argv[1])
    id = sys.argv[1]
    to_serialize_dict = {id: rows}
    with open(filename, 'w') as file:
        json.dump(to_serialize_dict, file)


if __name__ == '__main__':
    to_json()
