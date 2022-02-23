import json
import os

urls = []

os.system("clear")
ays = input("Are you sure you want to create these files? y/n: ")

if ays.lower() == "y":
    with open('url.json', 'w') as f:
        json.dump(urls, f)
        
    with open('logs.txt', 'w') as f:
        f.write("--Log File--")

    os.system("clear")
    cid = input("Please enter your client id:")
    os.system("clear")
    cs = input("Please enter your client secret:")
    os.system("clear")
    iu = input("Please enter your instagram username:")
    os.system("clear")
    ip = input("Please enter your instagram password:")
    os.system("clear")
    print("\nTime for some settings:\n")
    delay = input("Enter the delay for between posts (or type none to keep the default): ")
    if delay.lower() == "none":
        delay = 3
    else:
        try:
            int(delay)
        except:
            delay = 3

    show_hash = input("Should the bot show hastags in the caption (y/n): ")
    if show_hash.lower() not in ['y', 'n'] or show_hash.lower() == "y":
        show_hash = True
    else:
        show_hash = False

    show_subreddit = input("Should the bot show the subreddit in the caption (y/n): ")
    if show_subreddit.lower() not in ['y', 'n'] or show_subreddit.lower() == "y":
        show_subreddit = True
    else:
        show_subreddit = False

    data = {
        "show_subreddit" : show_subreddit,
        "show_hashtags" : show_hash,
        "wait_delay" : delay
    }
    with open("config.json", 'w') as f:
        json.dump(data, f, indent=4)
    

    with open('.env', 'w') as f:
        f.write(f"CLIENT_ID = {cid}\nCLIENT_SECRET = {cs}\ninsta_user = {iu}\ninsta_pass = {ip}")
    
    print("All files created successfully")
else:
    print("Ok")
print("Now downloading requirements")
os.system("pip install -r requirements.txt")