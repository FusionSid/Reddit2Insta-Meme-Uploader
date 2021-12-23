import json
import os

urls = []

ays = input("Are you sure you want to create these files? y/n: ")

if ays.lower() == "y":
    with open('url.json', 'w') as f:
        json.dump(urls, f)
        
    with open('logs.txt', 'w') as f:
        f.write("--Log File--")

    cid = input("Please enter your client id:")
    os.system("clear")
    cs = input("Please enter your client secret:")
    os.system("clear")
    iu = input("Please enter your instagram username:")
    os.system("clear")
    ip = input("Please enter your instagram password:")
    os.system("clear")

    with open('.ennv', 'w') as f:
        f.write()
else:
    print("Ok")