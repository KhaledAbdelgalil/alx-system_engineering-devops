#!/usr/bin/python3
"""
Function returns the titles of  hot
posts listed for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
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
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
