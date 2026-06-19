import snscrape.modules.twitter as sntwitter
import pandas as pd
import sys

# Arguments: ticker, since_date, until_date, max_tweets
ticker = sys.argv[1]  # e.g. 'AAPL'
since = sys.argv[2]   # e.g. '2025-09-01'
until = sys.argv[3]   # e.g. '2025-09-08'
max_tweets = int(sys.argv[4])  # e.g. 100

query = f"{ticker} since:{since} until:{until}"

tweets = []
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
    if i >= max_tweets:
        break
    tweets.append([tweet.date, tweet.content])

df = pd.DataFrame(tweets, columns=['Date', 'Tweet'])
output_file = f"{ticker}_tweets.csv"
df.to_csv(output_file, index=False)
print(f"Saved {len(df)} tweets to {output_file}")
