#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Return the total number of subscribers on a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The total number of subscribers of the subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "python:com.example.redditapi:v1.0.0 (by maina)"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx errors
        data = response.json()
        if 'data' in data and 'subscribers' in data['data']:
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            print("Unexpected response format:", data)
            return 0
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return 0


# Example usage:
subreddit_name = "python"
subscribers = number_of_subscribers(subreddit_name)
print("Number of subscribers in /r/{}: {}".format(subreddit_name, subscribers))

