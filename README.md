# Twitter Bot Detector

A Python tool that helps identify potential bot accounts on Twitter based on account characteristics and behavior patterns.

## Overview

This tool analyzes Twitter accounts using the Twitter API and evaluates them against several criteria commonly associated with automated accounts. It assigns a "bot score" based on how many bot-like characteristics are detected.

## Features

- Analyzes Twitter accounts using multiple detection criteria
- Provides a simple yes/no determination for bot accounts
- Uses Tweepy for seamless Twitter API integration

## Bot Detection Criteria

The tool checks for the following bot-like characteristics:

1. High tweet frequency (more than 10 tweets per day)
2. Unusual followers-to-following ratio (less than 1:5)
3. Empty or overly simple bio
4. Username containing symbols or numbers
5. Default profile picture
6. Recently created account (less than one year old)
7. No profile banner
8. Following specific political accounts (if you want to check other political accounts or any person, you can change the target_accounts list)

An account is classified as a bot if it exhibits 5 or more of these characteristics.

## Requirements

- Python 3.6+
- Tweepy library
- Twitter Developer Account with API credentials

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/sh1nnyboy/bot-identifies-fake-account-twitter.git
   cd bot-identifies-fake-account-twitter
   ```

2. Install the required dependencies:
   ```
   pip install tweepy
   ```

3. Add your Twitter API credentials to the script.

## Usage

1. Open `twitter_bot_detector.py` and replace the placeholder API credentials with your own.
2. Run the script:
   ```
   python twitter_bot_detector.py
   ```
3. Enter the Twitter username you want to analyze when prompted.

## Disclaimer

This tool provides an estimation based on common bot characteristics but is not definitive. Some legitimate accounts may exhibit bot-like characteristics, and sophisticated bots may evade detection.

## License

MIT License 
