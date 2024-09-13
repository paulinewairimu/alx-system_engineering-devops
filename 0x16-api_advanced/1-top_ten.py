#!/usr/bin/python3
"""Function to display the top 10 trending posts in a specified Reddit subreddit."""
import requests


def display_top_ten(subreddit):
    """Fetch and print the titles of the 10 most popular posts from a subreddit."""
    # Construct the Reddit API URL for hot posts in the subreddit
    api_url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    
    # Set headers to simulate a request from a web browser
    headers = {
        "User-Agent": "custom-scraper:v1.0.0 (by /u/your_username)"
    }
    
    # Set request parameters to limit the results to the top 10 posts
    params = {
        "limit": 10
    }
    
    # Send a GET request to fetch the subreddit data
    response = requests.get(api_url, headers=headers, params=params,
                            allow_redirects=False)
    
    # If the subreddit doesn't exist, print None and exit
    if response.status_code == 404:
        print("None")
        return
    
    # Extract and print the titles of the top 10 posts
    data = response.json().get("data")
    for post in data.get("children"):
        print(post.get("data").get("title"))

