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


def download_image(image_name, image_url, path_to_save='images/'):
    directory = path_to_save
    image_name = image_name
    image_url = image_url

    if not os.path.exists(directory):
        os.makedirs(directory)

    responce = requests.get(image_url)
    responce.raise_for_status()

    with open(f'{directory}{image_name}', 'wb') as file:
        file.write(responce.content)


def fetch_spacex_last_launch():
    spacex_api_url = 'https://api.spacexdata.com/v4/launches/'

    responce = requests.get(spacex_api_url)
    responce.raise_for_status()

    launch_spacex = responce.json()[13]
    if 'links' in launch_spacex:
        for url in launch_spacex['links']['flickr']['original']:
            download_image(create_filename(url), url)


def main():
    fetch_spacex_last_launch()


if __name__ == "__main__":
    main()
