#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import json
import requests
import sys

if __name__ == "__main__":
    userId = sys.argv[1]
    commonUrl = "https://jsonplaceholder.typicode.com/users/" + userId
    userData = requests.get(commonUrl).json()
    userTasks = requests.get(commonUrl + "/todos/").json()
    userName = userData.get("username")

    with open("{}.json".format(userId), "w") as jsonfile:
        json.dump({userId: [{
            "task": task["title"],
            "completed": task["completed"],
            "username": userData["username"]
        } for task in userTasks]
        }, jsonfile)
