#!/usr/bin/python3
"""query top 10 popular on a subreddit"""
import requests


def top_ten(subreddit):
    """ define API endpoint"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    """make the request"""
    response = requests.get(url, headers=headers)
    # If the response was successful, parse the JSON data
    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children'][:10]:
            print(post['data']['title'])
    else:
        print("None")
