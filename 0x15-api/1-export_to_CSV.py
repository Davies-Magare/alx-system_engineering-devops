#!/usr/bin/python3
"""
Request for data from an API and wrte it to file in CSV.
"""


import csv
import requests
import sys


def to_csv():
    """Write data to CSV file."""

    response = requests.get("https://jsonplaceholder.typicode.com/todos",
                            params={"userId": sys.argv[1]})
    response_name = requests.get("https://jsonplaceholder.typicode.com/users",
                                 params={"id": sys.argv[1]})
    dicts = response.json()
    name_dict = response_name.json()
    name = name_dict[0].get('username')
    id = sys.argv[1]

    comp = [[id, name, a_dict.get('completed'),
             a_dict.get('title')] for a_dict in dicts]
    keys = ['id', 'name', 'status', 'title']

    rows = []
    for lst in comp:
        row = {key: value for key, value in zip(keys, lst)}
        rows.append(row)
    filename = "{}.csv".format(sys.argv[1])
    with open(filename, 'w') as csvfl:
        write_obj = csv.DictWriter(csvfl, fieldnames=keys,
                                   quoting=csv.QUOTE_ALL)
        write_obj.writerows(rows)


if __name__ == '__main__':
    to_csv()
