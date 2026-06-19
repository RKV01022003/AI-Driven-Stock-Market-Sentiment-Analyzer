import praw
import pandas as pd
import sys

client_id = 'SI8pN3DSbt0zor'
client_secret = 'xaxkj7HNh8kwg8e5t4m6KvSrbTI'
user_agent = 'testscript by u/fakebot3'

# Arguments: subreddit, query, max_posts
subreddit_name = sys.argv[1]  # e.g. 'wallstreetbets'
query = sys.argv[2]           # e.g. 'AAPL'
max_posts = int(sys.argv[3])  # e.g. 50

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent)

subreddit = reddit.subreddit(subreddit_name)

posts = []
for i, submission in enumerate(subreddit.search(query, limit=max_posts)):
    posts.append([submission.title, submission.selftext, submission.created_utc])
    if i + 1 >= max_posts:
        break

df = pd.DataFrame(posts, columns=['Title', 'Body', 'Timestamp'])
output_file = f"{subreddit_name}_{query}_posts.csv"
df.to_csv(output_file, index=False)
print(f"Saved {len(df)} posts to {output_file}")
