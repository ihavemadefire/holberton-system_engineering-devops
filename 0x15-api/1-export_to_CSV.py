#!/usr/bin/python3
"""This script returns information about employee TODO list progress"""

import csv
import requests
import sys


if __name__ == "__main__":
    u = sys.argv[1]
    name = requests.get(
        "https://jsonplaceholder.typicode.com/users/" + u).json()
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos/?userId=" + u).json()
    file_name = '{}.csv'.format(u)
    csv.register_dialect('myDialect', quoting=csv.QUOTE_ALL)
    f = open(file_name, 'w')
    csv_writer = csv.writer(f, dialect='myDialect')
    for i in todos:
        us_id = i.get('userId')
        csv_writer.writerow(['{}'.format(i.get('userId')),
                             '{}'.format(name.get('username')),
                             '{}'.format(i.get('completed')),
                             '{}'.format(i.get('title'))])
    f.close()
