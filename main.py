# If you are reading this. I am so so so sorry that you have to read this piece of shit, buggy, not orginized code.

# fucking imports
import os
import json
from datetime import datetime
import time
from instabot import bot
import praw
from dotenv import load_dotenv
import wget
from datetime import datetime
import shutil

load_dotenv()

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
        shutil.rmtree("config")
        print("Cookies Eaten Successfuly.")
        log("Cookies Eaten Successfuly.")
    except Exception as e:
        print("Cookies Deletion Failed.")
        log(f"Cookies Deletion Failed. {e}")


# Create reddit client
def reddit_client():
    client = praw.Reddit(
        client_id=os.environ['CLIENT_ID'],
        client_secret=os.environ['CLIENT_SECRET'],
        user_agent="memes-fastapi"
    )
    return client


# Check if url is an image
def is_image(post):
    try:
        return post.post_hint == "image"
    except AttributeError:
        return False


# Get top 100 image urls (memes)
def get_img_url(client: praw.Reddit, subreddits: list, limit: int):
    memes = []
    for sub_name in subreddits:
        hot_memes = client.subreddit(sub_name).hot(limit=limit)

        for post in hot_memes:
            if is_image(post):
                data = {
                    "url": post.url,
                    "author": post.author.name,
                    "title": post.title
                }
                memes.append(data)

    return memes


log("----------START----------")
start_time = datetime.now()
# Notification for mac, If youre not on mac delete this line
os.system("""osascript -e 'display notification "Starting Meme Uploads" with title "Reddit 2 Insta"'""")
deletecookies()


# Create reddit client
client = reddit_client()

# get 100 image urls from each of these subreddits
rpsnlist = ['memes', 'dankmemes']
memes = get_img_url(client=client, subreddits=rpsnlist, limit=100)

log("Downloaded urls")

# Make insta bot
bot = bot.Bot()

# Login
bot.login(username=os.environ['insta_user'], password=os.environ['insta_pass'])

log("Logged In Successfully!")

hashtags = "#memes #funny #reddit #dankmemes #lol #memesdaily #humor #dank #meme #followorgetrickrolled #image #random #images"

old_count, new_count, gif_count = 0, 0, 0

for meme in memes:
    with open('urls.json', 'r') as f:
        data = json.load(f)

    post_url = meme["url"]
    post_author = meme["author"]
    post_title = meme["title"]

    fileext = post_url[-4] + post_url[-3] + post_url[-2] + post_url[-1]
    if fileext == '.gif':
        gif_count += 1
        continue

    if post_url in data:
        old_count += 1
        continue
    else:
        data.append(post_url)
        new_count += 1
        with open("urls.json", 'w') as f:
            json.dump(data, f, indent=4)

    filename = wget.download(url=str(post_url), out="upload")

    try:
        bot.upload_photo(
            filename, caption=f"{post_title}\nAuthor: {post_author}\n\n{hashtags}")
        time.sleep(2)
    except Exception as e:
        log(f"Error: {e}")
    os.remove(filename)

# Log
log(f"{new_count}/{len(rpsnlist)*100} new urls")
log(f"{old_count}/{len(rpsnlist)*100} old urls")
log(f"{gif_count}/{len(rpsnlist)*100} gifs")

deletecookies()

end_time = datetime.now()

total_time = int((end_time - start_time).total_seconds())

# Notification for mac, If youre not on mac delete this line
os.system(
    f"""osascript -e 'display notification "Finished in {total_time}s" with title "Reddit 2 Insta"'""")
log(f"Finished in {total_time}s")
log("-----------END-----------")
