# Reddit2Insta-Meme-Uploader

## The issue:

I have an instagram account where I post memes, The problem is that to post 1 meme I would have to got through reddit, find a meme I like, download it, post it, and lastly credit the author.

I did this for the first 300 memes on my page and then I bored and stoped posting.

But since I love to code I decided to make a script that can do this all for me :)

## **How to use & Setup:**

### 1. **Get your Client ID and Client Secret**
To get the `CLIENT_ID` and `CLIENT_SECRET` go to this [site](https://www.reddit.com/prefs/apps/) and create a new app. 

**App Settings:**

Choose script and make the name/description of the app whatever you want.

After that make the `redirect url` = `http://127.0.0.1:8000`

### 2. **Next create a `.env` file in the same directory as `main.py`**
### 3. **Add this to the `.env` file:**

```
CLIENT_ID = <Reddit client id> 
CLIENT_SECRET = <Reddit client secret>
insta_user = <Your instagram username>
insta_pass = <Your instagram password>
```

### 4. **Install all requirements**
```
pip install -r requirements.txt
```

### 5. **Clearing**

Delete `urls.json` and `log.txt`. Then run `new.py` It will ask you to confirm-just type `y` and then hit enter.

Next go to `main.py` and delete Line 128 (os.system('qc')), this line is a custom shell script I made but it won't work on your computer unless you download and set it up.

If you want to learn about this script, look/read [this](https://github.com/FusionSid/Shell-Scripts)

### 6. **Run/Done**
Yay youre done. If you followed the steps correctly you should be done. Now all you have to do is `python3 main.py` and the script will do everything by itself. If you turn up your volume the script will say "Done" once the script is done


**Note:** 

**Left Over Images:**
Sometimes the script will fail to delete an image after posting and might leave behing some images. If so just delete them or not. It won't affect the performance so it doesn't matter.

**Contributing**
If you have any suggestions for the script or want to make it better, Fork the repo and make your edits. Then make a pull request. I'll test it and if its good i'll add your edit to the script.

**Common Errors:**
While the script is running, many errors can occur. Most of the time its ok and as long as the script doesn't stop you should be fine. You can always read `log.txt`.
If you run the script to much you might get a rate limit ban. If so, please stop the script (if you dont the ban time will increase) and retry a day later. 


### **If you have any issues contact me!** 

**Im most active on discord so that would be a good way to message me
Discord Tag = `FusionSid#3645`**
