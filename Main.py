import VK.VK
import time
from Reddit.Reddit import RedditSession
from VK.VK import VK
import random

subbreddits = ['memes']

class PostMan:
    def __init__(self):
        self.log_dir = ''
        self.timer = 30 # in sec
        self.RedditSES = RedditSession(client_id = 'botid',
                                           client_secret = 'botsecrettoken',
                                           username = 'yourusername',
                                           password = 'yourpassword',
                                           user_agent = '214')#any number
        self.VKSES = VK('IDOFGROUP','IDOFALBUM','BOTTOKEN')
        ToPost = []
        while True:
            if len(ToPost) == 0:
                ToPost = self.RedditSES.GetPictures(random.choice(subbreddits), 3)
                print(ToPost)
            self.VKSES.Post(ToPost.pop(0))
            time.sleep(self.timer)

if __name__ == '__main__':
    Ses = PostMan()
