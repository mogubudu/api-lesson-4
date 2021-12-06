import os
import requests

from urllib.parse import urlparse, unquote


def get_filename(url):
    path = urlparse(url).path
    path = unquote(path)
    full_filename = os.path.basename(path)
    filename, extension = (os.path.splitext(full_filename)[0],
                           os.path.splitext(full_filename)[1])

    filename = filename.replace(' ', '_')
    return f'{filename}{extension}'


def check_folder_exist(folder_name):
    os.makedirs(folder_name, exist_ok=True)


def download_image(image_name, image_url, path_to_save):
    responce = requests.get(image_url)
    responce.raise_for_status()

    with open(f'{path_to_save}{image_name}', 'wb') as file:
        file.write(responce.content)
