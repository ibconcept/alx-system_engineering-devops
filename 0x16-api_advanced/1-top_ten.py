#!/usr/bin/python3

"""
Prints the titles of the first 10 hot posts listed for a given subreddit
"""

from requests import get

def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit
    """
    if not isinstance(subreddit, str):
        print("None")
        return

    user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
    params = {'limit': 10}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'

    try:
        response = get(url, headers=user_agent, params=params, allow_redirects=False)
        if response.status_code != 200:
            print("None")
            return
        
        results = response.json()
        my_data = results.get('data', {}).get('children', [])
        
        if not my_data:
            print("None")
            return
        
        for post in my_data:
            title = post.get('data', {}).get('title')
            if title:
                print(title)
            else:
                print("None")
    
    except Exception:
        print("None")

# Test the function with a real subreddit and a non-existent subreddit
if __name__ == "__main__":
    top_ten("python")  # Should print titles of the top 10 posts in r/python
    top_ten("nonexistentsubreddit123")  # Should print "None"

