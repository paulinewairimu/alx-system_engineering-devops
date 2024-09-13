#!/usr/bin/python3
"""Function to print the top 10 hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    
    # Define custom User-Agent to avoid request blocking
    headers = {
        "User-Agent": "custom-user-agent:v1.0.0 (by /u/your_username)"
    }
    
    # Limit to 10 posts
    params = {
        "limit": 10
    }
    
    # Send GET request to Reddit API
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    
    # Check if subreddit exists (status code 200), otherwise print None
    if response.status_code != 200:
        print("None")
        return
    
    # Extract the list of posts
    results = response.json().get("data", {}).get("children", [])
    
    # Print the title of each post or 'None' if no posts
    if results:
        for post in results:
            print(post.get("data", {}).get("title"))
    else:
        print("None")

