import praw
from newspaper import Article
from transformers import pipeline
import tweepy

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

user_agent = "Scraper 1.0"
reddit = praw.Reddit(
    client_id = "<Enter your Reddit App Client ID>",
    client_secret = "<Enter your Reddit App Client secret>",
    user_agent = user_agent
)

api_key = "<Enter your Twitter/X Consumer Key>"
api_secret = "<Enter your Twitter/X Consumer Secret>"
acctok = "<Enter your Twitter/X access token>"
acctok_secret = "<Enter your Twitter/X access token secret>"

client = tweepy.Client(
    consumer_key=api_key, consumer_secret=api_secret,
    access_token=acctok, access_token_secret=acctok_secret
)

counter = 0
for article in reddit.subreddit('Economics').hot(limit=10):
    if counter == 5:
        break
    art = Article(article.url)
    try:
        art.download()
        art.parse()
        if len(art.text) > 2000:
            body = summarizer(art.text, max_length=175, min_length=85, do_sample=False, truncation=True)[0].values()[0]
            response = client.create_tweet(
                text= "**" + article.title + "**\n" + body
            )
            print(f"https://twitter.com/user/status/{response.data['id']}")
            counter += 1
    except: 
        continue
