#!/usr/bin/python3
# function that queries the Reddit API and returns the number of subscribers

import requests


def number_of_subscribers(subreddit):
    # Reddit API URL for getting subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set custom User-Agent to avoid errors of Too Many Requests
    headers = {'User-Agent': 'Custom User Agent'}

    # Make a GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the number of subscribers from the JSON response
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    elif response.status_code == 404:
        # subreddit is not found
        return 0
    else:
        # Other errors
        print("Error occurred while fetching subreddit data.")
        return 0
