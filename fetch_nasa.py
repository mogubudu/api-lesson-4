import datetime as dt
import os
import requests

from dotenv import load_dotenv
from file_handler import download_image, get_filename, check_folder_exist


def download_image_from_nasa_apod(nasa_token,
                                  count=30,
                                  path_to_save='images/'):
    api_url = 'https://api.nasa.gov/planetary/apod'
    api_key = nasa_token
    params = {
      'api_key': api_key,
      'count': count,
    }

    check_folder_exist(path_to_save)

    responce = requests.get(api_url, params)
    responce = responce.json()

    for item in responce:
        if 'hdurl' in item:
            download_image(get_filename(item['hdurl']),
                           item['hdurl'], path_to_save)


def download_image_from_nasa_epic(nasa_token, path_to_save='images/'):
    api_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    api_key = nasa_token
    params = {
        'api_key': api_key,
    }

    check_folder_exist(path_to_save)

    responce = requests.get(api_url, params)
    responce = responce.json()

    for item in responce:
        if 'image' in item:
            full_date = item['date']
            formatted_date = dt.datetime.strptime(full_date,
                                                  '%Y-%m-%d %H:%M:%S')
            formatted_date = dt.datetime.strftime(formatted_date, '%Y/%m/%d')
            image_name = item['image']

            url_archive = (f'https://api.nasa.gov/EPIC/archive/natural/'
                           f'{formatted_date}/png/{image_name}.png'
                           f'?api_key={api_key}')

            download_image(get_filename(url_archive),
                           url_archive, path_to_save)


def main():
    load_dotenv()
    NASA_TOKEN = os.getenv('NASA_TOKEN')
    download_image_from_nasa_apod(NASA_TOKEN)
    download_image_from_nasa_epic(NASA_TOKEN)


if __name__ == "__main__":
    main()
