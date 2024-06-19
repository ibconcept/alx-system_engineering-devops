#!/usr/bin/python3
"""
Script to print hot posts on a given Reddit subreddit.
"""

import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            results = response.json().get("data")
            children = results.get("children", [])
            if not children:
                print("None")
                return
            for c in children:
                print(c.get("data").get("title"))
        else:
            print("None")
    except requests.RequestException as e:
        print("None")
    except ValueError:
        print("None")

# Test the function with a real subreddit and a non-existent subreddit
if __name__ == "__main__":
    top_ten("python")  # Should print titles of the top 10 posts in r/python
    top_ten("nonexistentsubreddit123")  # Should print "None"

