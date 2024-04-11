#!/usr/bin/python3
"""
a function that queries a subreddit andreturns no of subs
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of total subscribers for a
    given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    header = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    else:
        return 0
