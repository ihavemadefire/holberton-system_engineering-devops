#!/usr/bin/python3
"""This module returns a list of all tasks by user id  """

import json
import requests


if __name__ == "__main__":
    url_base = "https://jsonplaceholder.typicode.com/"
    names = requests.get(url_base + "users").json()
    json_dict = [{user.get("id"):
                  [{"task": i.get("title"),
                    "completed": i.get("completed"),
                    "username": user.get("username")}
                   for i in requests.get(url_base + "todos",
                                         params={"userId":
                                                 user.get("id")}).json()]
                  for user in names}]
    file_name = 'todo_all_employees.json'
    with open(file_name, 'w') as f:
        json.dump(json_dict, f)
