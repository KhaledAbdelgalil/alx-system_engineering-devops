#!/usr/bin/python3
"""
Function returns the titles of  hot
posts listed for a given subreddit
"""
import requests
after = None

def recurse(subreddit, hot_list=[]):
    """Returns a list of titles of all hot posts on a given subreddit."""
    global after
    if subreddit is None or type(subreddit) is not str:
        return None
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        'User-Agent': 'MyRedditAppApi/0.0.1 (by u/khaled)'
    }
    params = {
        "after": after,
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    if after is not None:
        recurse(subreddit, hot_list)
    
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))
    return hot_list
