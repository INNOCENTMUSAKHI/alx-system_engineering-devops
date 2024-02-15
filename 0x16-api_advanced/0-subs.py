import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom User Agent"}  # Provide a custom User-Agent header
    
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        
        # Check if the subreddit exists and return the number of subscribers
        if response.status_code == 200 and 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            return 0  # Return 0 for invalid or inaccessible subreddit
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return 0

# Example usage:
subreddit = "learnpython"  # Change this to any subreddit you want to check
print("Number of subscribers:", number_of_subscribers(subreddit))

