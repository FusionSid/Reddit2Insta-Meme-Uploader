# If you are reading this. I am so so so sorry that you have to read this piece of shit, buggy, not orginized code.

# fucking imports
import os
import json
import time
from instabot import bot
import praw
import dotenv
import glob
import wget
from datetime import datetime


# Logging cause i like too.
def log(log):
    now = datetime.now()
    timern = now.strftime("%d/%m/%Y %H:%M:%S")

    with open('log.txt', 'a') as f:
        f.write('\n')
        f.write(f"{timern} | {log}")

# For Deleting them damm cookies and other shit that keep comming
def deletecookies():
    try:
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

# Get top 100 image urls (memes)
def get_img_url(client: praw.Reddit, sub_name: str, limit: int):
    hot_memes = client.subreddit(sub_name).hot(limit=limit)
    image_urls = []
    for post in hot_memes:
        if is_image(post):
            image_urls.append(post.url)

    return image_urls


log("----------START----------")
deletecookies()
dotenv.load_dotenv()

# Create reddit client
client = reddit_client()

urls = []

# get 100 image urls from each of these subreddits
rpsnlist = ['memes', 'dankmemes']
for sub_reddit in rpsnlist:
    subred = sub_reddit
    url = get_img_url(client=client, sub_name=subred, limit=100) 
    urls.append(url)
    
log("Downloaded urls")
    
# Make insta bot
bot = bot.Bot()

# Login
bot.login(username=os.environ['insta_user'], password=os.environ['insta_pass'])

log("Logged In Successfully!")

# Choose an image and save it
ncount = 0
ocount = 0
gcount = 0
ht = "[#memes #funny #reddit #dankmemes #lol #memesdaily #humor #dank #meme #followorgetrickrolled #image #random #images]" # hastags
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
                    bot.upload_photo(filename, caption=f'Subreddit: {subred}\nCredit: {item}\n\n{ht}')
                    time.sleep(2)
                except Exception as e:
                    print(f"Error: {e}")
                    log(f"Error: {e}")
                os.remove(filename)

# Log
log(f"{ncount}/200 new urls")
log(f"{ocount}/200 old urls")
log(f"{gcount}/200 gifs")

deletecookies()
os.system("""osascript -e 'display notification "Finished" with title "Reddit 2 Insta"'""")
log("-----------END-----------")