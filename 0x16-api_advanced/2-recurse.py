#!/usr/bin/python3
""" return list of all hot articles in a subreddit """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Define the API endpoint URL with pagination"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    if after:
        url += f"?after={after}"
    # Define the request headers
    headers = {
        "User-Agent": "Mozilla/5.0"}

    # Make the request to the API and get the response
    response = requests.get(url, headers=headers)

    # If 200 parse JSON data and append the post titles to the hot_list
    if response.status_code == 200:
        data = response.json()
        for post in data["data"]["children"]:
            hot_list.append(post["data"]["title"])
        # Recurse with the next page of results
        if data["data"]["after"]:
            return recurse(subreddit, hot_list, data["data"]["after"])
        else:
            return hot_list
    else:
        return None
