import os
import requests

def download_image(url, filename):
    file_path = "images/"
    directory = os.path.dirname(file_path)
    try:
        os.stat(directory)
    except:
        os.mkdir(directory)
    response = requests.get(url)
    response.raise_for_status()
    with open(f'images/{filename}', 'wb') as file:
        file.write(response.content)

def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v3/launches'
    response = requests.get(url)
    data = response.json()
    images = list()
    for launch in reversed(data):
        launch_images = launch['links']['flickr_images']
        if launch_images:
            for image in launch_images:
                images.append(image)
            break
    for i, val in enumerate(images):
        download_image(val, f'spacex{i}.jpeg')



def main():
    fetch_spacex_last_launch()

if __name__ == "__main__":
    main()