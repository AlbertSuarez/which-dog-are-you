import argparse
import os
import shutil
import requests

from src import DATA_FOLDER, IMAGES_LIST_FILE_NAME, INDEX_FILE_NAME, INPUT_IMAGE_FILE_NAME


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_path', type=str)
    parser.add_argument('--image_url', type=str)
    parser.add_argument('--images_list_path', type=str, default=os.path.join(DATA_FOLDER, IMAGES_LIST_FILE_NAME))
    parser.add_argument('--index_file_path', type=str, default=os.path.join(DATA_FOLDER, INDEX_FILE_NAME))
    return parser.parse_args()


def run(image_path, image_url, images_list_path, index_file_path):
    # Check input
    if bool(image_path) == bool(image_url):
        print('You can only specify Image Path (x)or Image URL')
        return

    # Get image
    input_image_path = os.path.join(DATA_FOLDER, INPUT_IMAGE_FILE_NAME)
    if image_path:
        if not os.path.isfile(image_path):
            print(f'Image path provided does not exist: [{image_path}]')
            return
        shutil.copy(image_path, input_image_path)
    else:
        response = requests.get(image_url, verify=True, timeout=15, allow_redirects=True)
        if not response.ok:
            print(f'Image is not reachable using the given URL: [{image_url}]')
            return
        with open(input_image_path, 'w') as f:
            f.write(response.content)


if __name__ == '__main__':
    args = parse_args()
    run(args.image_path, args.image_url, args.images_list_path, args.index_file_path)
