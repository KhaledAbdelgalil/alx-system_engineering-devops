#!/usr/bin/python3
"""
Function returns the titles of hot
posts listed for a given subreddit
"""
import requests

after = None


def recurse(subreddit, hot_list=[]):
    """Returns a list of titles of all hot posts on a given subreddit."""
    global after
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        'User-Agent': 'khaled'
    }
    params = {"after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None

    results = response.json().get("data")
    after = results.get("after")
    titles = [c.get("data").get("title") for c in results.get("children")]
    hot_list.extend(titles)

    if after is not None:
        return recurse(subreddit, hot_list)
    return hot_list
