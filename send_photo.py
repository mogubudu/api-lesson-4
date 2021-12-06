import os
import time
import telegram

from dotenv import load_dotenv
from file_handler import check_folder_exist


def send_image_to_telegram_channel(telegram_token,
                                   channel_name,
                                   delay=86400,
                                   folder_name='images'):
    
    check_folder_exist(folder_name)

    bot = telegram.Bot(token=telegram_token)
    filenames = os.listdir(folder_name)

    for image_name in filenames:
        with open(f'{folder_name}/{image_name}', 'rb') as image_name:
            bot.send_document(chat_id=channel_name,
                              document=image_name)

            time.sleep(delay)


def main():
    load_dotenv()
    TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
    DELAY = int(os.getenv('DELAY_SLEEP'))
    CHANNEL_NAME = os.getenv('CHANNEL_NAME')
    send_image_to_telegram_channel(TELEGRAM_TOKEN, CHANNEL_NAME, DELAY)


if __name__ == "__main__":
    main()
