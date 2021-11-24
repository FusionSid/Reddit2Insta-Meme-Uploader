import requests

data = {'url':'google.com'}
url = "https://url-shortener.fusionsid.repl.co/api/"

for i in ['http://', 'https://']:
    if i in url:
        http = True
    else:
        http = False

if http == False:
    url = f"http://{url}"


response = requests.post(url, data=data)

if response.status_code == requests.codes.ok:
    print("Good")
else:
    print("Fail")

