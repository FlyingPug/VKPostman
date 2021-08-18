import praw
import urllib.request


class RedditSession:
    def __init__(self,client_id,client_secret,username,password,user_agent):
        self.Session = praw.Reddit(client_id = client_id,client_secret = client_secret, username = username,password = password,user_agent = user_agent)

    def GetPictures(self,SubName,length = 1):
        submissions = []
        i = 0
        while i < length:
            sub = self.Session.subreddit(SubName).random()
            if (sub.url.endswith("jpg") or sub.url.endswith("jpeg") or sub.url.endswith("png")):
                submissions.append(sub.url)
                i+=1
        return submissions