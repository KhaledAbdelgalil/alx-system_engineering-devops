#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    common_url = "https://jsonplaceholder.typicode.com/users/" + user_id
    userData = requests.get(common_url).json()
    userTasks = requests.get(common_url + "/todos/").json()
    tasks_titles = [t["title"] for t in userTasks if t["completed"] is True]
    print("Employee {} is done with tasks({}/{}):".format(
        userData["name"], len(tasks_titles), len(userTasks)))
    [print("\t {}".format(task_title)) for task_title in tasks_titles]
