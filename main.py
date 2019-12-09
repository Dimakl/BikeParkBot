#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Basic example for a bot that uses inline keyboards.
"""
import codecs
import logging

import json
import telegram

import maps
from telegram.ext import Updater, Filters, MessageHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def request_location(update, context):
    location_keyboard_find = telegram.KeyboardButton(text="Найди мне ближайшую парковку!", request_location=True)
    reply_markup = \
        telegram.ReplyKeyboardMarkup([[location_keyboard_find]])
    update.message.reply_text('Отправьте локацию или нажмите на кнопку:', reply_markup=reply_markup)

def compute_location(update, context):
    location = update.message.location
    location = [location['latitude'], location['longitude']]
    data = parse_json()
    point = maps.Path(location)
    nearest_points = point.find_n_nearest(3, data)
    print(nearest_points)
    images = []
    for i in range(1):
        image, distance, time_travel = point.gen_route_to(nearest_points[i])
        with open("image" + str(update.message.chat.id) + str(i), "wb") as f:
            f.write(image.read())
        images.append("image" + str(update.message.chat.id) + str(i))

    for image in images:
        context.bot.sendPhoto\
            (update.message.chat.id, open(image, 'rb'), caption="🚲 🅿 \nБлижайшая велопарковка в {} метрах! ({} мин.)".format(distance, time_travel))



def parse_json():
    all_dots = []

    with codecs.open('VeloParkData.json', 'r', 'utf-8-sig') as f:
        off_data = json.load(f)
    for obj in off_data:
        all_dots.append(obj['geoData']['coordinates'][::-1])

    return all_dots


def main():

    REQUEST_KWARGS = {
        'proxy_url': 'socks5://185.73.240.95:1080',

        'urllib3_proxy_kwargs': {
            'username': 'k4proxy',
            'password': 'sosipisos8464'
        }
    }

    updater = Updater(TOKEN, use_context=True, request_kwargs=REQUEST_KWARGS)

    updater.dispatcher.add_handler(MessageHandler(Filters.text, request_location))
    updater.dispatcher.add_handler(MessageHandler(Filters.command, request_location))
    updater.dispatcher.add_handler(MessageHandler(Filters.location, compute_location))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()

