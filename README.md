# Tweet Archiver
## Before you start
Using the free API, you will only be able to retrieve ~3.2k tweets. If you purchase the upgraded API you can get all of them.

I have tried using different techniques to retrieve all of a user's tweets, such as:
- Using Selenium to scroll through a user's timeline (it stops you after a certain amount)
- Using Selenium to search in day increments from the user's account creation time to the current date (it simply does not show tweets on days that there were tweets
- Using the Twitter Search API rather than the User API, which claims to have no limit (it cuts you off after ~1k tweets

This is the only limitation of this script. If you have a way around it, please open an issue.

# Setup

**Requirements**:

- Git
- Python 2.7
- Pip for Python2.7
- Twitter API keys

1. Get your Twitter API keys from https://apps.twitter.com

2. Clone the repository and initialise pip modules:

**Note: Syntax may differ depending on how you setup Python 2.7, pip2 and pipenv2**

```bash
git clone https://github.com/anomiee/tweet_archiver.git
pipenv2 install
```

3. Open the file `tweet_archiver.py` and insert the following information:

```python
# EDIT THIS!
# Twitter API credentials - https://apps.twitter.com/
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""`
```

4. Run the script with the target twitter username as the argument:

```bash
python2 tweet_archiver.py target_username
