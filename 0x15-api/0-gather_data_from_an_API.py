#!/usr/bin/python3
"""
script that uses a REST API for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
import sys


if __name__ == "__main__":
    """
    crawls the API and returns the employee progress
    """
    user_id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_str = '{}users/{}'.format(base_url, user_id)
    todos_str = '{}todos?userId={}'.format(base_url, user_id)
    employee_str = "Employee {} is done with tasks"

    res = requests.get(user_str)
    print(employee_str.format(res.json().get('name')), end="")

    res = requests.get(todos_str)
    tasks = []
    for task in res.json():
        if task.get('completed') is True:
            tasks.append(task)

    print("({}/{}):".format(len(tasks), len(res.json())))
    for task in tasks:
        print("\t {}".format(task.get("title")))
