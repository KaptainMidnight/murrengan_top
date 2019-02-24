# -*- coding: utf-8 -*-

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from utils_1 import get_random_id
import db

vk_session = vk_api.VkApi(token="c0a9ae78d65852efad873d0ae29664145911b961e34fcaf83939e9bac3d8dd284dc65b11a058aacf36011")

vk = vk_session.get_api()

longpool = VkLongPoll(vk_session)

while True:
    for event in longpool.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            response = event.text.lower()
            if response == "баланс":
                b = db.get_user_stats(event.user_id)
                print("44")
                vk.messages.send(peer_id=event.peer_id, random_id=get_random_id(),
                                     message="Привет, твой баланс: " + int(b["money"]))
                vk.messages.send(peer_id=event.peer_id, random_id=get_random_id(),
                                     message="Произошла непредвиденная ошибка, повторите позже")
