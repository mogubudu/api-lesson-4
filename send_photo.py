import os
import time
import telegram

from dotenv import load_dotenv


def send_image_to_telegram_channel(telegram_token,
                                   channel_name,
                                   delay=86400,
                                   folder_name='images'):

    bot = telegram.Bot(token=telegram_token)
    filenames = os.listdir(folder_name)

    for image_name in filenames:
        with open(f'{folder_name}/{image_name}', 'rb') as filename:
            bot.send_document(chat_id=channel_name,
                              document=filename)

            time.sleep(delay)


def main():
    load_dotenv()
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    delay = int(os.getenv('DELAY_SLEEP'))
    channel_name = os.getenv('CHANNEL_NAME')
    send_image_to_telegram_channel(telegram_token, channel_name, delay)


if __name__ == "__main__":
    main()
