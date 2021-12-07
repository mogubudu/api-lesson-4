import os
import requests

from urllib.parse import urlparse, unquote


def get_filename(url):
    path = urlparse(url).path
    path = unquote(path)
    full_filename = os.path.basename(path)

    filename = full_filename.replace(' ', '_')
    return f'{filename}'


def download_image(image_name, image_url, path_to_save):
    responce = requests.get(image_url)
    responce.raise_for_status()

    with open(f'{path_to_save}{image_name}', 'wb') as file:
        file.write(responce.content)
