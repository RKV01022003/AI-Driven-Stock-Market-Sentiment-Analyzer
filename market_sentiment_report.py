import pandas as pd
import sys

if len(sys.argv) != 3:
    print("Usage: python market_sentiment_report.py twitter_file reddit_file")
    sys.exit(1)

twitter_file = sys.argv[1]
reddit_file = sys.argv[2]

twitter_df = pd.read_csv(twitter_file)
reddit_df = pd.read_csv(reddit_file)

twitter_score = twitter_df['Sentiment_Score'].mean()
reddit_score = reddit_df['Sentiment_Score'].mean()

overall_score = (twitter_score + reddit_score) / 2

if overall_score > 0.05:
    market_sentiment = "POSITIVE"
elif overall_score < -0.05:
    market_sentiment = "NEGATIVE"
else:
    market_sentiment = "NEUTRAL"

print("\n" + "=" * 50)
print("AI DRIVEN STOCK MARKET SENTIMENT REPORT")
print("=" * 50)

print(f"\nTwitter Average Sentiment : {twitter_score:.3f}")
print(f"Reddit Average Sentiment  : {reddit_score:.3f}")
print(f"Overall Sentiment Score   : {overall_score:.3f}")

print(f"\nMarket Mood : {market_sentiment}")

print("\n" + "=" * 50)