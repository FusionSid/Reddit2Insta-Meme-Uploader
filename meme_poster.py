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

def delete_image(image):
    if image.endswith('.jpg'):
        os.remove(image)
    elif image.endswith('.png'):
        os.remove(image)
    elif image.endswith('.REMOVE_ME'):
        os.remove(image)
    else:
        print("Can't find image")

deletecookies()

dotenv.load_dotenv()

# Create reddit client
def reddit_client():
    client = praw.Reddit(
        client_id= os.environ['CLIENT_ID'],
        client_secret = os.environ['CLIENT_SECRET'],
        user_agent = os.environ['USER_AGENT']
    )
    return client

# Get top 50 image urls (memes)
def get_img_url(client: praw.Reddit, sub_name: str, limit: int):
    hot_memes = client.subreddit(sub_name).hot(limit=limit)
    image_urls = []
    for post in hot_memes:
        image_urls.append(post.url)
    return image_urls

# Get the urls
client = reddit_client()
urls = get_img_url(client=client, sub_name='memes', limit=1)

# Make insta bot
bot = bot.Bot()

# Login
bot.login(username=os.environ['insta_user'], password=os.environ['insta_pass'])

def get_random():
    amount = 25
    for i in range(amount):
        image = random.choice(urls)
        response = requests.get(image)
        with open('image.png', 'wb') as f:
            f.write(response.content)
            f.close()

# Choose an image and save it

for item in urls:
    response = requests.get(item, stream=True)
    fileext = item[-4] + item[-3] + item[-2] + item[-1]
    #filename = item.split('/')[-1]
    filename = 'image'+fileext
    with open(filename,'wb') as f:
        f.write(response.content)
        f.close()

    image = f'{filename}'

    # Upload photo
    try:
        bot.upload_photo(image, caption='')
        print("Done")
    except:
        print("Upload Failed")

    delete_image(image)
deletecookies()
