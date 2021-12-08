import json

urls = []

ays = input("Are you sure you want to create these files? y/n: ")

if ays.lower() == "y":
    with open('urls.json', 'w') as f:
        json.dump(urls, f)
        
    with open('log.txt', 'w') as f:
        f.write("--Log File--")
else:
    print("Ok")