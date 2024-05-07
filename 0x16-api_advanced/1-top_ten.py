#!/usr/bin/python3
# function that queries the Reddit API
# prints the titles of the first 10 hot posts listed for a given subreddit
# If not a valid subreddit, print None

import requests


def top_ten(subreddit):
    # Reddit API URL for getting hot posts in a subreddit
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    # Set custom User-Agent to avoid errors of Too Many Requests
    headers = {'User-Agent': 'Custom User Agent'}

    # Make a GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the titles of the first 10 hot posts
        data = response.json()
        posts = data['data']['children']
        for i in range(10):
            print("{}. {}".format(i + 1, posts[i]['data']['title']))
    elif response.status_code == 404:
        # If not a valid subreddit
        print("None")
    else:
        # Other errors
        print("Error occurred while fetching subreddit data.")
