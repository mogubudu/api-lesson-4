import os
import requests

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


def check_folder_exist(folder_name):
    os.makedirs(folder_name, exist_ok=True)

def download_image(image_name, image_url, path_to_save):
    responce = requests.get(image_url)
    responce.raise_for_status()

    with open(f'{path_to_save}{image_name}', 'wb') as file:
        file.write(responce.content)

