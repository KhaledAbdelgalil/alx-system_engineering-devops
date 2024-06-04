#!/usr/bin/python3
"""
Function returns the titles of  hot
posts listed for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=""):
    """returns the titles of 10 hot
    posts listed for a given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return None
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        'User-Agent': 'MyRedditAppApi/0.0.1 (by u/khaled)'
    }
    params = {
        "count": count,
        "after": after,
        "limit": 50
    }
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code == 404:
        return None
    results = response.json().get("data")
    after = results.get("after")
    for res in results.get("children"):
        hot_list.append(res.get("data").get("title"))
        count += 1
    if after is not None:
        return recurse(subreddit, hot_list, count, after)
    return hot_list
