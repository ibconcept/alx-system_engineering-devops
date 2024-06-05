#!/usr/bin/python3
'''
    This module contains the function top_ten
'''

import requests
from sys import argv


def top_ten(subreddit):
    '''
        Returns the top ten posts for a given subreddit
    '''

    user_agent = {'User-Agent': 'MyRedditScript/1.0'}

    url = ('https://www.reddit.com/r/{}/hot/.json?'
           'limit=10'.format(subreddit))

    try:
        response = requests.get(url, headers=user_agent)
        response.raise_for_status()  # Raise an exception for HTTP errors

        data = response.json()

        for post in data.get('data').get('children'):
            print(post.get('data').get('title'))

    except requests.HTTPError as e:
        print("HTTP error occurred:", e)
    except requests.RequestException as e:
        print("Request exception occurred:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)


if __name__ == "__main__":
    subreddit_name = argv[1] if len(argv) > 1 else None
    if subreddit_name:
        top_ten(subreddit_name)
    else:
        print("Please provide a subreddit name as a command-line argument.")
