import subprocess

ticker = input("Enter Stock Ticker (Example: AAPL): ").upper()

start_date = input("Start Date (YYYY-MM-DD): ")
end_date = input("End Date (YYYY-MM-DD): ")

print("\nDownloading Stock Data...")

subprocess.run(
    [
        "python",
        "download_stock.py",
        ticker,
        start_date,
        end_date
    ],
    check=True
)

print("\nCollecting Tweets...")

subprocess.run(
    [
        "python",
        "scrape_tweets.py",
        ticker,
        start_date,
        end_date,
        "100"
    ],
    check=True
)

print("\nCollecting Reddit Posts...")

subprocess.run(
    [
        "python",
        "scrape_reddit.py",
        "wallstreetbets",
        ticker,
        "50"
    ],
    check=True
)

print("\nRunning Sentiment Analysis...")

twitter_file = f"{ticker}_tweets.csv"

reddit_file = f"wallstreetbets_{ticker}_posts.csv"

subprocess.run(
    [
        "python",
        "sentiment_analysis.py",
        twitter_file
    ],
    check=True
)

subprocess.run(
    [
        "python",
        "sentiment_analysis.py",
        reddit_file
    ],
    check=True
)

print("\nGenerating Final Report...")

subprocess.run(
    [
        "python",
        "market_sentiment_report.py",
        f"{ticker}_tweets_sentiment.csv",
        f"wallstreetbets_{ticker}_posts_sentiment.csv"
    ],
    check=True
)

print("\nProject Execution Completed Successfully.")