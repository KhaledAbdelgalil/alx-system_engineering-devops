#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys
import csv

if __name__ == "__main__":
    userId = sys.argv[1]
    commonUrl = "https://jsonplaceholder.typicode.com/users/" + userId
    userData = requests.get(commonUrl).json()
    userTasks = requests.get(commonUrl + "/todos/").json()
    userName = userData["name"]
    with open(f"{userId}.csv", "w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [
            writer.writerow(
                [userId, userName, task["completed"], task["title"]]
            ) for task in userTasks
        ]
