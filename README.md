# NewsCompilerTwitterBot
## Automated a Twitter/X bot that posts crowd-sourced trending economic news every day using Reddit API, Natural Language Processing Model (BERT), and Twitter/X API

Full code can be found in the main branch. For privacy/security purposes, the API keys and secrets will not be provided. To implement something similar, replace API keys and secrets with one's own keys. This can be done by creating a developer app on Twitter & Reddit.

Automated the process of getting crowd-sourced trending/important economic news every day and made it available for everyone on Twitter/X. Instead of having to scroll through reddit or google news, click through each of the links, and read through the entire article before realizing that you weren't interested and it was a waste of time, go on twitter/X follow @A_SH0O and get all the information you need in just 5 tweets!

The bot goes through the subreddit "Economics" and finds the top 5 "Hot" posts that day. From there it visits the news article URL present in each of the posts and proceeds to parse the article to retrieve only the body contents. These body contents are then passed to a Natural Language Processor (BERT) to summarize the data to around an 80 word excerpt. The data is then passed to the Twitter/X API to create a tweet.

The result is a tweet containing a thread of the Headline, the 80 word summary of the article, and a link to the article for further reading if needed. This is a much more appealing way of digesting information rather than being shoved full on news articles in your face.

**Dependencies**:

Reddit API: Used to scrape subreddits to find relevant articles

PRAW: Reddit API wrapper to better access API endpoints using Python

newspaper3k: Python library to download news articles through URLs as well as parse and retrieve the body content

transformers: Downloaded the Natural Language Processing Model (BERT) to summarize the news article `summarizer = pipeline("summarization", model="facebook/bart-large-cnn")`

TwitterAPI: Used to post a thread of tweets containing the headline, summary, and a link to the article

Tweepy: Twitter API wrapper to better access API endpoints using Python

