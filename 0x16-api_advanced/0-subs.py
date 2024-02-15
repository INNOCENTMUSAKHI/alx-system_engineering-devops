#!/usr/bin/python3
"""
This module contains the function number_of_subscribers.
"""

import requests
import sys

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    """
    user_agent = "MyBot/1.0"  # Set your own User-Agent here
    headers = {"User-Agent": user_agent}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for 4xx or 5xx status codes
        data = response.json()
        return data["data"]["subscribers"]
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        print(number_of_subscribers(subreddit))

