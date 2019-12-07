#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Basic example for a bot that uses inline keyboards.
"""
import logging

import telegram
from telegram.ext import Updater, Filters, MessageHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def request_location(update, context):
    location_keyboard = telegram.KeyboardButton(text="send_location", request_location=True)
    reply_markup = telegram.ReplyKeyboardMarkup([[location_keyboard]])

    update.message.reply_text('Отправьте локацию:', reply_markup=reply_markup)


def compute_location(update, context):
    location = update.message.location
    print(location)


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