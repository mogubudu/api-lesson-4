import datetime as dt
import os
import requests

from dotenv import load_dotenv
from urllib.parse import urlparse, unquote


def get_file_extencion(url):
    path = urlparse(url)[2]
    path = unquote(path)
    extencion = os.path.splitext(path)[1]
    return extencion


def get_filename(url):
    path = urlparse(url)[2]
    path = unquote(path)
    filename = os.path.split(path)[1]
    filename = os.path.splitext(filename)[0]
    filename = filename.replace(' ', '_')
    return filename


def create_filename(url):
    filename = get_filename(url)
    extencion = get_file_extencion(url)
    return f'{filename}{extencion}'


def download_image(image_name, image_url, path_to_save):
    directory = path_to_save
    image_name = image_name
    image_url = image_url

    if not os.path.exists(directory):
        os.makedirs(directory)

    responce = requests.get(image_url)
    responce.raise_for_status()

    with open(f'{directory}{image_name}', 'wb') as file:
        file.write(responce.content)


def download_image_from_nasa_apod(nasa_token,
                                  count=30,
                                  path_to_save='images/'):
    api_url = 'https://api.nasa.gov/planetary/apod'
    api_key = nasa_token
    params = {
      'api_key': api_key,
      'count': count,
    }

    responce = requests.get(api_url, params)
    responce = responce.json()

    for item in responce:
        if 'hdurl' in item:
            download_image(create_filename(item['hdurl']),
                           item['hdurl'], path_to_save)


def download_image_from_nasa_epic(nasa_token, path_to_save='images/'):
    api_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    api_key = nasa_token
    params = {
        'api_key': api_key,
    }

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

            download_image(create_filename(url_archive),
                           url_archive, path_to_save)


def main():
    load_dotenv()
    NASA_TOKEN = os.getenv('NASA_TOKEN')
    download_image_from_nasa_apod(NASA_TOKEN)
    download_image_from_nasa_epic(NASA_TOKEN)


if __name__ == "__main__":
    main()
