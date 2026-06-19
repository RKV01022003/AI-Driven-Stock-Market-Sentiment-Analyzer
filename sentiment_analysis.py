import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import sys

analyzer = SentimentIntensityAnalyzer()

if len(sys.argv) != 2:
    print("Usage: python sentiment_analysis.py <csv_file>")
    sys.exit(1)

input_file = sys.argv[1]

df = pd.read_csv(input_file)

if 'Title' in df.columns and 'Body' in df.columns:
    df['Text'] = (
        df['Title'].fillna('').astype(str) +
        ' ' +
        df['Body'].fillna('').astype(str)
    )
elif 'Tweet' in df.columns:
    df['Text'] = df['Tweet'].fillna('').astype(str)
else:
    raise Exception("No valid text column found")

def get_sentiment(text):
    return analyzer.polarity_scores(text)['compound']

df['Sentiment_Score'] = df['Text'].apply(get_sentiment)

def label(score):
    if score > 0.05:
        return 'Positive'
    elif score < -0.05:
        return 'Negative'
    return 'Neutral'

df['Sentiment'] = df['Sentiment_Score'].apply(label)

output_file = input_file.replace(".csv", "_sentiment.csv")

df.to_csv(output_file, index=False)

print(f"Sentiment file saved: {output_file}")
print(df['Sentiment'].value_counts())