import json
import os

urls = []

os.system("clear")
ays = input("Are you sure you want to create these files? y/n: ")

if ays.lower() == "y":
    with open('urls.json', 'w') as f:
        json.dump(urls, f)
        
    with open('log.txt', 'w') as f:
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

    with open('.env', 'w') as f:
        f.write(f"CLIENT_ID = {cid}\nCLIENT_SECRET = {cs}\ninsta_user = {iu}\ninsta_pass = {ip}")
    
    print("All files created successfully")
else:
    print("Ok")
print("Now downloading requirements")
os.system("pip install -r requirements.txt")