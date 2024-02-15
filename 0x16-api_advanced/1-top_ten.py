#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""

import requests


def fetch_posts(subreddit, limit=10):
    """
    Fetches the top hot posts from the given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        limit (int): The number of posts to fetch. Default is 10.

    Returns:
        list: A list of post titles.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Custom"}
    params = {"limit": limit}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json().get("data", {}).get("children", [])
        return [post["data"]["title"] for post in data]
    except requests.HTTPError:
        print(f"Error: Failed to fetch posts from r/{subreddit}")
        return []

def print_top_ten(subreddit):
    """
    Prints the titles of the top 10 hot posts from the given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
    """
    posts = fetch_posts(subreddit)
    if posts:
        print(f"Top 10 hot posts in r/{subreddit}:")
        for i, title in enumerate(posts, start=1):
            print(f"{i}. {title}")
    else:
        print(f"No posts found in r/{subreddit}")

# Example usage:
if __name__ == "__main__":
    subreddit = input("Enter the name of the subreddit: ")
    print_top_ten(subreddit)

