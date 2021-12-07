import os
import requests
from file_handler import download_image, get_filename


def fetch_spacex_last_launch(path_to_save='images/', index_of_launch=13):
    spacex_api_url = 'https://api.spacexdata.com/v4/launches/'

    os.makedirs(path_to_save, exist_ok=True)

    responce = requests.get(spacex_api_url)
    responce.raise_for_status()

    launch_spacex = responce.json()[index_of_launch]
    if 'links' in launch_spacex:
        for url in launch_spacex['links']['flickr']['original']:
            download_image(get_filename(url), url, path_to_save)


def main():
    fetch_spacex_last_launch()


if __name__ == "__main__":
    main()
