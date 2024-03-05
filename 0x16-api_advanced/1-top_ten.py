#!/usr/bin/python3
"""returns hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = { "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    params = { "limit": 10 }

    rep = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if rep.status_code == 404:
        print("None")
        return
    res = rep.json().get("data")
    [print(c.get("data").get("title")) for c in res.get("children")]
