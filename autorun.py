# Dont use this

import os
import json
import time
from instabot import bot as bot
import praw
import dotenv
import glob
import wget
from datetime import datetime

from keep_alive import keep_alive

def log(log):
    now = datetime.now()
    timern = now.strftime("%d/%m/%Y %H:%M:%S")

    with open('log.txt', 'a') as f:
        f.write('\n')
        f.write(f"{timern} | {log}")


def deletecookies():
    try:
        # Delete them damm cookies and other shit that keep comming
        cookie_del = glob.glob("config/*cookie.json")
        os.remove(cookie_del[0])
        print("Cookies Eaten Successfuly.")
        log("Cookies Eaten Successfuly.")
    except:
        print("Cookies Deletion Failed.")
        log("Cookies Deletion Failed.")


# Create reddit client
def reddit_client():
    client = praw.Reddit(
        client_id= os.environ['CLIENT_ID'],
        client_secret = os.environ['CLIENT_SECRET'],
        user_agent = "memes-fastapi"
    )
    return client

# Check if url is an image
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

    return image_urls

# ----------Start------------

def main():
    log("----------START----------")
    deletecookies()
    dotenv.load_dotenv()

    # Create reddit client
    client = reddit_client()

    urls = []

    # get 50 image urls from each of these subreddits
    rpsnlist = ['memes', 'dankmemes']
    for sub_reddit in rpsnlist:
        subred = sub_reddit
        url = get_img_url(client=client, sub_name=subred, limit=100) 
        urls.append(url)
        
    log("Downloaded urls")
        
    # Make insta bot
    ibot = bot.Bot()

    # Login
    ibot.login(username=os.environ['insta_user'], password=os.environ['insta_pass'])

    log("Logged In Successfully!")

    # Choose an image and save it
    ncount = 0
    ocount = 0
    gcount = 0
    for item in urls:
        for item in item:
            # get file extension jpg, png, gif, etc
            fileext = item[-4] + item[-3] + item[-2] + item[-1]
            with open('urls.json', 'r') as f:
                data = json.load(f)
            if item in data:
                pass  
                ocount += 1
            else:
                data.append(item)
                with open('urls.json', 'w') as f:
                    json.dump(data, f, indent=4)
                ncount += 1
                if fileext == '.gif':
                    pass
                    gcount += 1
                else:
                    filename = wget.download(url=str(item))
                    # Upload photo
                    try:
                        ibot.upload_photo(filename, caption=f'Subreddit: {subred}\nCredit: {item}')
                        time.sleep(2)
                    except Exception as e:
                        print(f"Error: {e}")
                        log((f"Error: {e}"))
                    os.remove(filename)

    # Log
    log(f"{ncount}/200 new urls")
    log(f"{ocount}/200 old urls")
    log(f"{gcount}/200 gifs")

    # os.system('qc')

    deletecookies()
    log("-----------END-----------")


keep_alive()
while True:
    main()
    time.sleep(43200)
    os.system("git pull")
    os.system("git add .")
    os.system("git commit -m 'e'")
    os.system("git push")