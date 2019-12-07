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
    location_keyboard_find = telegram.KeyboardButton(text="Найди мне парковку!", request_location=True)
    location_keyboard_add = \
        telegram.KeyboardButton(text="Я стою на парковке и хочу добавить ее !")
    reply_markup = telegram.ReplyKeyboardMarkup([[location_keyboard_find], [location_keyboard_add]])

    update.message.reply_text('Отправьте локацию:', reply_markup=reply_markup)


def compute_location(update, context):
    location = update.message.location
    location = [location['longitude'], location['latitude']]
    data = parse_json()
    point = maps.Path(location)
    nearest_points = point.find_n_nearest(3, data)
    print(nearest_points)
    for coords in nearest_points:
        image = point.gen_route_to(coords)
        file = image.read()
        with open("test", "wb") as f:
            f.write(file)


def parse_json():
    all_dots = []

    with codecs.open('VeloParkData.json', 'r', 'utf-8-sig') as f:
        off_data = json.load(f)
    for obj in off_data:
        all_dots.append(obj['geoData']['coordinates'])

    return all_dots


def main():

    REQUEST_KWARGS = {
        'proxy_url': 'socks5://185.73.240.95:1080',

        'urllib3_proxy_kwargs': {
            'username': 'k4proxy',
            'password': 'sosipisos8464'
        }
    }

    updater = Updater("956994519:AAHNHMkrKR3D4ppbe-mLOCdVIDM1aHBFSuQ", use_context=True, request_kwargs=REQUEST_KWARGS)

    updater.dispatcher.add_handler(MessageHandler(Filters.text, request_location))
    updater.dispatcher.add_handler(MessageHandler(Filters.location, compute_location))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()

