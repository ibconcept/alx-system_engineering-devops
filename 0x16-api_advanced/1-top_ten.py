#!/usr/bin/python3

from requests import get


def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")
        return

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    try:
        response = get(url, headers=user_agent, params=params)
        if response.status_code != 200:
            print("None")
            return

        results = response.json()
        my_data = results.get('data', {}).get('children', [])

        if not my_data:
            print("None")
            return

        for post in my_data:
            print(post.get('data', {}).get('title', 'None'))

    except Exception as e:
        print("None")


# Example usage
top_ten("python")

