import vk_api
import requests
import os


class VK:
    def __init__(self,GroupId,AlbumId,VKBOTtoken):
        self.vk_session = vk_api.VkApi(token=VKBOTtoken)
        self.GroupId = GroupId
        self.AlbumId = AlbumId
        self.VKBOTtoken = VKBOTtoken
    def Post(self,link):
        upload = vk_api.VkUpload(self.vk_session)
        v = requests.get(link)
        open(link.rsplit('/', 1)[1], 'wb').write(v.content)
        r = upload.photo(photos=link.rsplit('/', 1)[1], group_id=self.GroupId, caption="", album_id=self.AlbumId)
        attach = str(r[0]['id'])
        d = requests.post('https://api.vk.com/method/wall.post', data={
            'access_token': self.VKBOTtoken,
            'owner_id': '-' + (self.GroupId),
            'from_group': 1,
            'message': '#reddit',
            ##minecraft #reddit #meme #memes #shitpost #cursed #майнкрафт
            'signed': 0,
            #'copyright':link,
            'attachments': 'photo' + '-'+self.GroupId+ '_' + attach,
            'v': "5.52"}).json()
        os.remove(link.rsplit('/', 1)[1])