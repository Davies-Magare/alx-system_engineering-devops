#!/usr/bin/python3
"""
Request for data from an API and wrte it to file in json.
"""


import csv
import json
import requests
import sys


def to_json_all():
    """Write all employee data to json file."""

    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    dicts = response.json()
    ids = []
    for a_dict in dicts:
        if a_dict['userId'] not in ids:
            ids.append(a_dict['userId'])
    to_serialize_dict = {}
    for id in ids:
        response = requests.get("https://jsonplaceholder.typicode.com/todos",
                                params={"userId": id})
        dicts = response.json()
        query_str = "https://jsonplaceholder.typicode.com/users"
        response_name = requests.get(query_str, params={"id": id})
        name_dict = response_name.json()
        name = name_dict[0].get('username')
        comp = [[a_dict.get('title'),
                 a_dict.get('completed'), name] for a_dict in dicts]
        keys = ['task', 'completed', 'username']

        rows = []
        for lst in comp:
            row = {key: value for key, value in zip(keys, lst)}
            rows.append(row)
        to_serialize_dict[id] = rows

    filename = "todo_all_employees.json"
    with open(filename, 'w') as file:
        json.dump(to_serialize_dict, file)


if __name__ == '__main__':
    to_json_all()
