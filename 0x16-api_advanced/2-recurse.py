#!/usr/bin/python3
"""a query for a list of all hot posts on a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = { "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    rep = requests.get(url, headers=headers, params=params, allow_redirects=False)

    res = rep.json().get("data")
    after = res.get("after")
    count += res.get("dist")
    for c in res.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list 
