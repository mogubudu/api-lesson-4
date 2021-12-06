import requests
from file_handler import download_image, create_filename

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
