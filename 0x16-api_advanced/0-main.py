#!/usr/bin/python3
"""
0-main
"""
import sys

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    """
    try:
        import requests
        headers = {'User-Agent': 'Lizzie'}
        url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return data['data']['subscribers']
    except Exception as e:
        print("Error making API request:", e)
        return 0

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        print("{:d}".format(number_of_subscribers(subreddit)))

