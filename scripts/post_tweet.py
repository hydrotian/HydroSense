#!/usr/bin/env python3
"""Post a tweet to X (Twitter) via API v2."""

import argparse
import os
import re
import sys
from dotenv import load_dotenv
from requests_oauthlib import OAuth1Session

# X counts every URL as 23 characters (t.co shortening)
TCO_URL_LENGTH = 23
URL_PATTERN = re.compile(r'https?://\S+|hydrosense\.simhydro\.com\S*')


def count_tweet_length(text):
    """Count tweet length with t.co URL shortening applied."""
    without_urls = URL_PATTERN.sub('', text)
    url_count = len(URL_PATTERN.findall(text))
    return len(without_urls) + (url_count * TCO_URL_LENGTH)


def truncate_tweet(text, max_length=280):
    """Truncate tweet text while preserving the URL at the end."""
    if count_tweet_length(text) <= max_length:
        return text

    urls = URL_PATTERN.findall(text)
    body = URL_PATTERN.sub('', text).rstrip()

    if urls:
        url = urls[-1]
        # Available chars: max - URL(23) - newlines(2) - ellipsis(3)
        available = max_length - TCO_URL_LENGTH - 5
        if len(body) > available:
            truncated = body[:available]
            # Try to break at last complete sentence
            last_period = truncated.rfind('.')
            last_paren = truncated.rfind(').')
            break_at = max(last_period, last_paren + 1) if last_paren > 0 else last_period
            if break_at > available * 0.5:
                body = truncated[:break_at + 1]
            else:
                last_space = truncated.rfind(' ')
                body = truncated[:last_space] + '...'
        return f"{body}\n\n{url}"
    else:
        return text[:277] + '...'


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

    length = count_tweet_length(args.text)
    if length > 280:
        print(f"Warning: Tweet is {length} chars (max 280), truncating...", file=sys.stderr)
        args.text = truncate_tweet(args.text)
        print(f"Truncated to {count_tweet_length(args.text)} chars", file=sys.stderr)

    post_tweet(args.text)


if __name__ == '__main__':
    main()
