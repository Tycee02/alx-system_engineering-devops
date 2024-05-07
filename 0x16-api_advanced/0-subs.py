#!/usr/bin/python3
# function that queries the Reddit API and returns the number of subscribers

import requests
import sys


def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'Custom User Agent'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return (response.json().get("data").get("subscribers"))
    return (0)
