# AI-Driven Stock Market Sentiment Analyzer

## Overview

The AI-Driven Stock Market Sentiment Analyzer is a Python-based project that collects stock market data and analyzes public sentiment from social media platforms. The project combines stock price information, Twitter discussions, and Reddit posts to determine overall market sentiment for a selected stock ticker.

This project demonstrates data collection, sentiment analysis, data processing, and basic financial analytics using Python.

---

## Features

* Download historical stock price data from Yahoo Finance.
* Collect stock-related tweets.
* Scrape Reddit discussions from investment communities.
* Perform sentiment analysis using VADER Sentiment Analyzer.
* Generate sentiment-labeled datasets.
* Produce a consolidated market sentiment report.
* Fully automated execution through a single pipeline.

---

## Project Structure

```text
AI-Driven-Stock-Market-Sentiment-Analyzer/

│
├── download_stock.py
├── scrape_tweets.py
├── scrape_reddit.py
├── sentiment_analysis.py
├── market_sentiment_report.py
├── main.py
│
├── requirements.txt
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/AI-Driven-Stock-Market-Sentiment-Analyzer.git

cd AI-Driven-Stock-Market-Sentiment-Analyzer
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## How It Works

### Step 1: Download Stock Data

Historical stock prices are downloaded using Yahoo Finance.

Output:

```text
AAPL_prices.csv
```

---

### Step 2: Collect Tweets

Twitter posts mentioning the selected stock ticker are collected.

Output:

```text
AAPL_tweets.csv
```

---

### Step 3: Collect Reddit Posts

Posts related to the stock ticker are collected from Reddit communities.

Output:

```text
wallstreetbets_AAPL_posts.csv
```

---

### Step 4: Sentiment Analysis

The project analyzes tweets and Reddit discussions using the VADER sentiment model.

Output:

```text
AAPL_tweets_sentiment.csv

wallstreetbets_AAPL_posts_sentiment.csv
```

Additional columns generated:

* Sentiment_Score
* Sentiment

Possible labels:

* Positive
* Negative
* Neutral

---

### Step 5: Market Sentiment Report

The average sentiment from Twitter and Reddit is combined to generate an overall market sentiment score.

Example Output:

```text
==================================================
AI DRIVEN STOCK MARKET SENTIMENT REPORT
==================================================

Twitter Average Sentiment : 0.314

Reddit Average Sentiment  : 0.427

Overall Sentiment Score   : 0.371

Market Mood : POSITIVE
==================================================
```

---

## Running the Project

Execute the complete pipeline:

```bash
python main.py
```

The program will ask for:

```text
Stock Ticker
Start Date
End Date
```

Example:

```text
Enter Stock Ticker: AAPL

Start Date: 2025-01-01

End Date: 2025-12-31
```

---

## Workflow

```text
Stock Ticker
      │
      ▼

Download Stock Data
      │
      ▼

Collect Tweets
      │
      ▼

Collect Reddit Posts
      │
      ▼

Sentiment Analysis
      │
      ▼

Generate Market Report
      │
      ▼

Final Sentiment Score
```

---

## Sample Output Files

```text
AAPL_prices.csv

AAPL_tweets.csv

AAPL_tweets_sentiment.csv

wallstreetbets_AAPL_posts.csv

wallstreetbets_AAPL_posts_sentiment.csv
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* Yahoo Finance API
* SNScrape
* Reddit API (PRAW)
* VADER Sentiment Analysis

---

## Future Enhancements

* FinBERT-based sentiment analysis
* Real-time market monitoring
* News sentiment integration
* Machine learning-based stock prediction
* Streamlit dashboard
* Data visualization and reporting

---

## Disclaimer

This project is intended for educational and research purposes only. The generated sentiment scores and analyses should not be considered financial advice. Investment decisions should be made after conducting independent research and consulting qualified financial professionals.

---

## Author

Rishu Kumar

B.Tech – Computer Science & Engineering

Machine Learning | Artificial Intelligence | Data Science
