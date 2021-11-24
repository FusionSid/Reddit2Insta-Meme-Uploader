import os
from instabot import bot
import random
import praw
import requests
import dotenv
import glob

def deletecookies():
    try:
        # Delete them damm cookies and other shit that keep comming
        cookie_del = glob.glob("config/*cookie.json")
        os.remove(cookie_del[0])
    except:
        print("Error")

dotenv.load_dotenv()

# Create reddit client
def reddit_client():
    client = praw.Reddit(
        client_id= os.environ['CLIENT_ID'],
        client_secret = os.environ['CLIENT_SECRET'],
        user_agent = os.environ['USER_AGENT']
    )
    return client

def is_image(post):
    try:
        return post.post_hint == "image"
    except AttributeError:
        return False

# Get top 50 image urls (memes)
def get_img_url(client: praw.Reddit, sub_name: str, limit: int):
    hot_memes = client.subreddit(sub_name).hot(limit=limit)
    image_urls = []
    for post in hot_memes:
        if is_image(post):
            image_urls.append(post.url)
            print(post.url)
    return image_urls

# Get the urls
client = reddit_client()

rpsnlist = ['memes', 'dankmemes', 'MemeEconomy', 'darkhumor' ]
subred = input("Which subreddit/random: ")
if subred.lower() == "random":
    subred = random.choice(rpsnlist)
else:
    subred = subred
print(subred)

urls = get_img_url(client=client, sub_name=subred, limit=50)

# Make insta bot
bot = bot.Bot()

# Login
bot.login(username=os.environ['insta_user'], password=os.environ['insta_pass'])

# Choose an image and save it
for item in urls:
    response = requests.get(item, stream=True)
    fileext = item[-4] + item[-3] + item[-2] + item[-1]
    if fileext == '.gif':
        pass
    else:
        filename = 'image'+fileext
        with open(filename,'wb') as f:
            f.write(response.content)
            f.close()

        image = f'{filename}'

        # Upload photo
        try:
            bot.upload_photo(image, caption=f'Subreddit: {subred}')
            os.remove(image)
            print("Done")
        except:
            print("Upload Failed")

deletecookies()