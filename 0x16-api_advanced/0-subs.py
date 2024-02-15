#!/usr/bin/python3
'''
    This module contains the function number_of_subscribers
'''
import requests
from sys import argv


def number_of_subscribers(subreddit):
    '''
    Returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit, or 0 if the subreddit is invalid
             or an error occurs.

    Raises:
        requests.exceptions.RequestException: If an error occurs while making the API request.
        json.JSONDecodeError: If there is an error decoding the JSON response.
    '''
    user_agent = {'User-Agent': 'Reddit API Client by YourUsername'}
    try:
        response = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json', headers=user_agent)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    except requests.exceptions.RequestException as e:
        print(f'Error making API request: {e}')
        return 0
    except json.JSONDecodeError as e:
        print(f'Error decoding JSON response: {e}')
        return 0
    except KeyError:
        print(f"Subreddit '{subreddit}' not found or blocked.")
        return 0


if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: python3 <script.py> <subreddit>")
    else:
        subreddit = argv[1]
        subscribers = number_of_subscribers(subreddit)
        print(f"The subreddit '{subreddit}' has {subscribers} subscribers.")

