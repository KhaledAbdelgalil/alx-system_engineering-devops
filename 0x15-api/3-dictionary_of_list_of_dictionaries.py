#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import json
import requests

if __name__ == "__main__":
    commonUrl = "https://jsonplaceholder.typicode.com/users/"
    users = requests.get(commonUrl).json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            user["id"]: [{
                "username": user["username"],
                "task": task["title"],
                "completed": task["completed"]}
                for task in
                requests.get(commonUrl + str(user["id"]) + "/todos").json()
                ] for user in users}, jsonfile)
