# Reddit2Insta-Meme-Uploader

## The issue:

---

I have an instagram account where I post memes, The problem is that to post 1 meme I would have to got through reddit, find a meme I like, download it, post it, and lastly credit the author.

I did this for the first 300 memes on my page and then I bored and stoped posting.

But since I love to code I decided to make a script that can do this all for me :)

Here is my insta account for an example: [Account](https://www.instagram.com/never_gonnagive/)

---

## **How to use & Setup:**

To use this bot you will need `python` and `pip` installed. Most of the time they are already installed on your system.
Download from the releases tab on this github.

---

### 1. **Get your Client ID and Client Secret**
To get the `CLIENT_ID` and `CLIENT_SECRET` go to this [site](https://www.reddit.com/prefs/apps/) and create a new app. 

---

**App Settings:**

Choose script and make the name and description of the app whatever you want.

After that make the `redirect url` = `http://127.0.0.1:8000`

---

### 2. **Setup Files**
Now run `python3 setup.py` and type `y` to confirm. This script will setup all files needed for the bot to run. The script will ask you to enter your `Client ID`, `Client Secret`, `Instagram Username` and `Instagram Password`. Please enter all of them or the bot will not work.

---

### 3. **Run/Done**
Yay you're done. If you followed the steps correctly everything should be ready for you to start posting some memes. Now all you have to do is `python3 main.py` and the script will do everything by itself. 

---

## **Extra:** 

---

**Left Over Images:**
Sometimes the script will fail to delete an image after posting and might leave behing some images. If so just delete them or not. It won't affect the performance so it doesn't matter.

---

**Contributing**
If you have any suggestions for the script or want to make it better, Fork the repo and make your edits. Then make a pull request. I'll test it and if its good i'll add your edit to the script.

---

**Common Errors:**
While the script is running, many errors can occur. Most of the time its ok and as long as the script doesn't stop you should be fine. You can always read `log.txt`.

If you run the script to much you might get a rate limit ban. It might say something like `too many requests trying again in 5 minutes` If so, please stop the script (if you dont the ban time will increase) and retry a day later. 

Incase after running `setup.py` all requirements are not downloaded, just run:
```
pip install -r requirements.txt
```
and it should download everthing needed.

---

## **If you have any issues contact me!** 

**Im most active on discord so that would be a good way to message me
Discord Tag = `FusionSid#3645`**

---

![](readme_images/example.png)