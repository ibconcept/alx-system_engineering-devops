import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.

    Args:
    subreddit (str): The name of the subreddit.

    Returns:
    None
    """
    # Set a generic user-agent header
    headers = {'User-Agent': 'MyRedditScript/1.0'}

    # Construct the URL for the API request
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json?limit=10'

    try:
        # Send a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the response is successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Extract and print the titles of the first 10 hot posts
            for post in data.get('data', {}).get('children', [])[:10]:
                print(post.get('data', {}).get('title'))
        else:
            # Print None if the subreddit is not valid or there is another issue
            print("None")
    except Exception as e:
        # Print None if there is an exception
        print("None")

# Example usage
if __name__ == "__main__":
    subreddit = input("Enter the name of the subreddit: ")
    top_ten(subreddit)

