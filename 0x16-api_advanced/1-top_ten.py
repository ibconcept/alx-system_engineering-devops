#!/usr/bin/python3
'''
    This module contains the function top_ten.
'''

import requests
from sys import argv

def top_ten(subreddit):
    '''
    Returns the titles of the first 10 hot posts for a given subreddit.
    '''
    user_agent = {'User-Agent': 'MyRedditBot/1.0'}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json?limit=10'
    
    try:
        response = requests.get(url, headers=user_agent, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for any HTTP error status codes
        
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        
        if not posts:
            print("No posts found for the subreddit:", subreddit)
            return
        
        for post in posts:
            print(post.get('data', {}).get('title'))
    
    except requests.HTTPError as e:
        print("Error accessing subreddit:", e)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 script.py subreddit_name")
    else:
        top_ten(argv[1])

