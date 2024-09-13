#!/usr/bin/python3
"""
Script to fetch a list of popular posts from a given subreddit on Reddit.
"""

import requests


def fetch_hot_posts(subreddit, post_titles=[], pagination_token="", post_count=0):
    """
    Recursively fetches a list of popular post titles from a subreddit.

    Args:
        subreddit (str): The subreddit name to query.
        post_titles (list, optional): A list to accumulate the post titles.
                                      Defaults to an empty list.
        pagination_token (str, optional): The token to track pagination.
                                          Defaults to an empty string.
        post_count (int, optional): Tracks the number of posts retrieved.
                                    Defaults to 0.

    Returns:
        list: A list of post titles from the hot section of the subreddit.
    """
    # Formulate the URL for fetching the subreddit's hot posts in JSON format
    request_url = f"https://www.reddit.com/r/{subreddit}/hot/.json"

    # Set headers to mimic a legitimate browser request
    headers = {
        "User-Agent": "custom-reddit-scraper:v1.0.0 (by /u/your_username)"
    }

    # Parameters to control pagination and the number of posts retrieved
    params = {
        "after": pagination_token,
        "count": post_count,
        "limit": 100
    }

    # Perform the GET request to retrieve the subreddit data
    response = requests.get(request_url, headers=headers, params=params,
                            allow_redirects=False)

    # Check if the subreddit exists or if the request was unsuccessful
    if response.status_code == 404:
        return None

    # Extract relevant information from the JSON response
    response_data = response.json().get("data")
    pagination_token = response_data.get("after")
    post_count += response_data.get("dist")

    # Add each post title to the list
    for post in response_data.get("children"):
        post_titles.append(post.get("data").get("title"))

    # Recursively retrieve more posts if the pagination token exists
    if pagination_token:
        return fetch_hot_posts(subreddit, post_titles, pagination_token, post_count)

    # Return the complete list of post titles
    return post_titles

