#!/usr/bin/python3
"""This module takes in an  """

import json
import requests
import sys


if __name__ == "__main__":
    u = sys.argv[1]
    name = requests.get(
        "https://jsonplaceholder.typicode.com/users/" + u).json()
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos/?userId=" + u).json()
    info = [{"task": i.get("title"),
             "completed": i.get("completed"),
             "username": name.get("username")}
            for i in todos]
    json_dict = {}
    json_dict[u] = info
    file_name = '{}.json'.format(u)
    with open(file_name, 'w') as f:
        json.dump(json_dict, f)
