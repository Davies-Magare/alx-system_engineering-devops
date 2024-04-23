#!/usr/bin/python3
"""
Request for data from an API and utilize it.
"""
import requests
import sys


def gather_data():
    """Gather data from API and utilize it."""

    response = requests.get("https://jsonplaceholder.typicode.com/todos",
                            params={"userId": sys.argv[1]})
    response_name = requests.get("https://jsonplaceholder.typicode.com/users",
                                 params={"id": sys.argv[1]})
    dicts = response.json()
    name_dict = response_name.json()
    comp = [a_dict for a_dict in dicts if a_dict.get('completed') is True]
    print("Employee {} is done with tasks ({}/{}):"
          .format(name_dict[0].get('name'), len(comp), len(dicts)))
    for a_dict in comp:
        print("\t{}".format(a_dict.get('title')))


if __name__ == '__main__':
    gather_data()
