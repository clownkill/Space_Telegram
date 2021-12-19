import os
import requests
from urllib.parse import urlsplit
from datetime import datetime
from dotenv import load_dotenv


def fetch_file_extension(url):
    url_file_path = urlsplit(url).path
    file_name = os.path.split(url_file_path)[-1]
    file_extension = os.path.splitext(file_name)[-1]
    return file_extension


def download_image(url, filename, dirname=''):
    file_path = f'images/{dirname}/'
    directory = os.path.dirname(file_path)
    try:
        os.stat(directory)
    except:
        os.mkdir(directory)
    response = requests.get(url)
    response.raise_for_status()
    with open(f'images/{dirname}/{filename}', 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v3/launches'
    response = requests.get(url)
    data = response.json()
    images = []
    for launch in reversed(data):
        launch_images = launch['links']['flickr_images']
        if launch_images:
            for image in launch_images:
                images.append(image)
            break
    for i, val in enumerate(images):
        download_image(val, f'spacex{i}.jpeg', dirname='SpaceX')


def fetch_nasa_image(token):
    url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': token,
        'count': 50,
    }
    response = requests.get(url, params=params)
    data = response.json()
    for i, val in enumerate(data):
        file_extension = fetch_file_extension(val['url'])
        file_name = f'NASA{i}{file_extension}'
        download_image(val['url'], file_name, dirname='NASA')


def fetch_nasa_epic_image(token):
    params = {
        'api_key': token,
    }
    url_to_parsed = 'https://api.nasa.gov/EPIC/api/natural'
    images_info = []
    response = requests.get(url_to_parsed, params=params)
    epic_data = response.json()
    date = ''
    for rec in epic_data:
        images_info.append(rec['image'])
        date = rec['date']
    epic_date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S').date()
    year = epic_date.year
    month = epic_date.month
    day = epic_date.day
    for image in images_info:
        url = f'https://epic.gsfc.nasa.gov/archive/natural/{year}/{month}/{day}/png/{image}.png'
        file_extension = fetch_file_extension(url)
        download_image(url, f'epic_{image}{file_extension}', dirname='NASO_EPIC')


def main():
    load_dotenv()
    nasa_token = os.environ['NASA_API']
    fetch_spacex_last_launch()
    fetch_nasa_image(nasa_token)
    fetch_nasa_epic_image(nasa_token)


if __name__ == "__main__":
    main()
