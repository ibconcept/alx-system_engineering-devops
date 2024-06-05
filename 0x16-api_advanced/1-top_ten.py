#!/usr/bin/python3
"""
Module to fetch and print titles of the first 10 hot posts in a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.
    """
    if not subreddit or not isinstance(subreddit, str):
        print("None")
        return

    user_agent = {'User-agent': 'Mozilla/5.0'}
    params = {'limit': 10}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'

    try:
        response = requests.get(url, headers=user_agent, params=params, allow_redirects=False)
        if response.status_code != 200:
            print("None")
            return

        results = response.json()
        posts = results.get('data', {}).get('children', [])

        if not posts:
            print("None")
            return

        for post in posts:
            print(post.get('data', {}).get('title', 'None'))

    except Exception as e:
        print("None")


