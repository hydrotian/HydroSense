#!/usr/bin/env python3
"""Post a tweet to X (Twitter) via API v2."""

import argparse
import os
import sys
from dotenv import load_dotenv
from requests_oauthlib import OAuth1Session


def post_tweet(text):
    """Post a tweet and return the tweet URL, or None on failure."""
    load_dotenv()

    api_key = os.getenv('X_API_KEY')
    api_secret = os.getenv('X_API_SECRET')
    access_token = os.getenv('X_ACCESS_TOKEN')
    access_secret = os.getenv('X_ACCESS_TOKEN_SECRET')

    if not all([api_key, api_secret, access_token, access_secret]):
        print("Error: X API credentials not configured in .env", file=sys.stderr)
        return None

    oauth = OAuth1Session(api_key, api_secret, access_token, access_secret)

    # Get username for tweet URL
    user_resp = oauth.get('https://api.x.com/2/users/me')
    if user_resp.status_code != 200:
        print(f"Error getting user info: {user_resp.status_code}", file=sys.stderr)
        return None
    username = user_resp.json()['data']['username']

    # Post tweet
    resp = oauth.post('https://api.x.com/2/tweets', json={'text': text})

    if resp.status_code == 201:
        tweet_id = resp.json()['data']['id']
        url = f"https://x.com/{username}/status/{tweet_id}"
        print(f"Tweet posted: {url}")
        return url
    else:
        print(f"Error posting tweet: {resp.status_code}", file=sys.stderr)
        print(resp.json(), file=sys.stderr)
        return None


def main():
    parser = argparse.ArgumentParser(description='Post a tweet to X')
    parser.add_argument('text', help='Tweet text (max 280 characters)')
    args = parser.parse_args()

    if len(args.text) > 280:
        print(f"Warning: Tweet is {len(args.text)} chars (max 280), truncating...", file=sys.stderr)
        args.text = args.text[:277] + '...'

    post_tweet(args.text)


if __name__ == '__main__':
    main()
