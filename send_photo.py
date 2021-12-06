import os
import time
import telegram

from dotenv import load_dotenv


def send_image_to_telegram_channel(telegram_token,
                                   channel_name,
                                   delay=86400,
                                   folder_name='images'):
    directory = folder_name
    if not os.path.exists(directory):
        os.makedirs(directory)

    bot = telegram.Bot(token=telegram_token)
    channel_name = channel_name
    filenames = os.listdir(directory)

    for image_name in filenames:
        with open(f'{directory}/{image_name}', 'rb') as image_name:
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
