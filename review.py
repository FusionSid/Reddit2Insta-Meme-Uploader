import os
import json
import time
from instabot import bot
import praw
import dotenv
import glob
import wget
from PIL import Image

def deletecookies():
    try:
        # Delete them damm cookies and other shit that keep comming
        cookie_del = glob.glob("config/*cookie.json")
        os.remove(cookie_del[0])
        print("Cookies Eaten Successfuly.")
    except:
        print("Cookies Deletion Failed.")

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
    counter = 0
    for post in hot_memes:
        if is_image(post):
            print(counter)
            image_urls.append(post.url)
            counter += 1

    return image_urls


# Create reddit client
client = reddit_client()

urls = []

# get 50 image urls from each of these subreddits
rpsnlist = ['memes', 'dankmemes']
for sub_reddit in rpsnlist:
    subred = sub_reddit

    url = get_img_url(client=client, sub_name=subred, limit=50) 
    urls.append(url)
    
# Make insta bot
bot = bot.Bot()

# Login
bot.login(username=os.environ['insta_user'], password=os.environ['insta_pass'])

# Choose an image and save it
for item in urls:
    for item in item:
        # get file extension jpg, png, gif, etc
        fileext = item[-4] + item[-3] + item[-2] + item[-1]
        with open('urls.json', 'r') as f:
            data = json.load(f)
        if item in data:
            pass
        else:
            data.append(item)
            with open('urls.json', 'w') as f:
                json.dump(data, f, indent=4)
        if fileext == '.gif':
            pass
        else:
            filename = wget.download(url=str(item))
            review = input("Type 'r' to review or 'p' to ignore and post\n")
            if review.lower() == 'r':
                Img=Image.open(filename)
                Img.show()
                delete = input("Type 'd' to delete or 'p' to ignore and post\n")
                if delete.lower() == 'd':
                    os.remove(filename)
                else:
                    # Upload photo
                    try:
                        bot.upload_photo(filename, caption=f'Subreddit: {subred}\nCredit: {item}')
                        time.sleep(2)
                        os.remove(filename)
                        time.sleep(2)
                    except Exception as e:
                        print(f"Error: {e}")
                os.system('killall Preview')
            else:
                # Upload photo
                try:
                    bot.upload_photo(filename, caption=f'Subreddit: {subred}\nCredit: {item}')
                    time.sleep(2)
                    os.remove(filename)
                    time.sleep(2)
                except Exception as e:
                    print(f"Error: {e}")
            
            
deletecookies()