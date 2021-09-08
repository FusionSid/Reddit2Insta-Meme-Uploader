import os
import random
import praw
import requests
import dotenv

dotenv.load_dotenv()

def reddit_client():
    client = praw.Reddit(
        client_id= os.environ['CLIENT_ID'],
        client_secret = os.environ['CLIENT_SECRET'],
        user_agent = os.environ['USER_AGENT']
    )
    return client

def get_img_url(client: praw.Reddit, sub_name: str, limit: int):
    hot_memes = client.subreddit(sub_name).hot(limit=limit)
    image_urls = []
    for post in hot_memes:
        image_urls.append(post.url)
    return image_urls

client = reddit_client()
urls = get_img_url(client=client, sub_name='memes', limit=50)

image = random.choice(urls)

response = requests.get(image)
with open('image.png', 'wb') as f:
    f.write(response.content)
    f.close()