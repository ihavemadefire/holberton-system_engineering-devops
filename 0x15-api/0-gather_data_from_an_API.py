#!/usr/bin/python3
"""This script returns information about employee TODO list progress"""

import requests
import sys

if __name__ == "__main__":
    u = sys.argv[1]
    names = requests.get(
        "https://jsonplaceholder.typicode.com/users/" + u).json()
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos/?userId=" + u).json()
    total = len(todos)
    completed = [i for i in todos if i.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(names.get("name"),
                                                          len(completed),
                                                          total))
    for i in completed:
        print("\t {}".format(i.get("title")))
