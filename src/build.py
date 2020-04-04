import argparse
import glob
import os

from src import DATA_FOLDER, DATASET_FOLDER, IMAGES_LIST_FILE_NAME, INDEX_FILE_NAME
from src.helper import keras, index


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset_folder', type=str, default=os.path.join(DATA_FOLDER, DATASET_FOLDER))
    parser.add_argument('--images_list_path', type=str, default=os.path.join(DATA_FOLDER, IMAGES_LIST_FILE_NAME))
    parser.add_argument('--index_file_path', type=str, default=os.path.join(DATA_FOLDER, INDEX_FILE_NAME))
    return parser.parse_args()


def _get_images(dataset_folder):
    images = glob.glob(os.path.join(dataset_folder, '*.jpg'))
    print(f'Images: {len(images)}')
    return images


def build(dataset_folder, images_list_path, index_file_path):
    images = _get_images(dataset_folder)
    features = keras.extract_features(images, images_list_path)
    index.build(features, index_file_path)


if __name__ == '__main__':
    args = parse_args()
    build(args.dataset_folder, args.images_list_path, args.index_file_path)
