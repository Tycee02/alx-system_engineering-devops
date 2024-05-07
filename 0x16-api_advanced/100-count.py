#!/usr/bin/python3
""" recursive function that queries the Reddit API"""
import requests
import sys
after = None
count_dic = []


def count_words(subreddit, word_list):
    """parses the title of all hot articles, and prints a sorted count of given
    keywords (case-insensitive, delimited by spaces) """
    global after
    global count_dic
    headers = {'User-Agent': 'xica369'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=parameters)

    posts = data['data']['children']
    for post in posts:
        title = post['data']['title'].lower()
        for word in word_list:
            if re.search(r'\b{}\b'.format(word.lower()), title):
                word_count[word.lower()] =
                word_count.get(word.lower(), 0) + 1

    word_items = word_count.items()
    after = data['data']['after']
    if after:
        count_words(subreddit, word_list, after, word_count)
    else:
        sorted_word_count = sorted(word_items, key=lambda x: (-x[1], x[0]))
    for word, count in sorted_word_count:
        print("{}: {}".format(word, count))
        else:
            return None
