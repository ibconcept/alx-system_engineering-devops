#!/usr/bin/python3
'''
Module for retrieving the top ten posts from a subreddit.
'''
import requests
import sys

def top_ten(subreddit):
    '''
    Retrieves the top ten posts for a given subreddit.
    '''
    user_agent = {'User-Agent': 'MyRedditScript/1.0'}
    try:
        response = requests.get(f'https://www.reddit.com/r/{subreddit}/hot/.json?limit=10',
                                headers=user_agent)
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
    subreddit_name = sys.argv[1] if len(sys.argv) > 1 else None
    if subreddit_name:
        top_ten(subreddit_name)
    else:
        print("Please provide a subreddit name as a command-line argument.")

