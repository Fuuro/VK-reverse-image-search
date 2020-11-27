from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.longpoll import VkLongPoll, VkEventType
import requests
import io

def sender(id,text):
    vkSession.method('messages.send', {'peer_id' : id, 'message' : text, 'random_id': 0})

while True:
    vkSession = VkApi(token='')
    longPoll = VkBotLongPoll(vkSession, group_id=)
    vk = vkSession.get_api()

    try:
        for event in longPoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                atchs = event.object['attachments']
            
                if atchs:
                    for atch in atchs:
                        if atch['type'] == 'photo':
                           photo = atch['photo']
                            url = photo['sizes'][-1]['url']
                            url=url.split("?")[0]
                            count=url.count('/')
                            url2=url.split('/')
                            url = url.replace(url2[3]+'/', "")
                            img = requests.get(url).content
                            f = io.BytesIO(img)
                            id = event.obj['peer_id']
                            sauce = ('\n\n' + 'Saucenao: '+  'https://saucenao.com/search.php?url=' + url + '\n' + '\n' + 'Google: ' + 'https://www.google.com/searchbyimage?&image_url=' + url + '\n' + '\n' + 'Yandex: ' + 'https://yandex.ru/images/search?source=collections&rpt=imageview&url=' + url + '\n\n' + 'Если ищите аниме по кадру:' + 'https://trace.moe/?mute&url=' + url + "\n\n"  )
                            sender(id, sauce)
    except Exception:
        pass
