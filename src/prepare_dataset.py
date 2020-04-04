import argparse
import glob
import os
import random
import shutil
import zipfile

from src import DATA_FOLDER, DATA_INPUT_ZIP, DATA_OUTPUT_ZIP, DEFAULT_IMAGES_PER_RACE, DATASET_FOLDER


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--images_per_race', type=int, default=DEFAULT_IMAGES_PER_RACE)
    parser.add_argument('--input_zip_path', type=str, default=os.path.join(DATA_FOLDER, DATA_INPUT_ZIP))
    parser.add_argument('--output_zip_folder', type=str, default=os.path.join(DATA_FOLDER, DATA_OUTPUT_ZIP))
    parser.add_argument('--dataset_folder', type=str, default=os.path.join(DATA_FOLDER, DATASET_FOLDER))
    parser.add_argument('--force_unzip', action='store_true')
    return parser.parse_args()


def _unzip(input_zip_path, output_zip_folder, force_unzip):
    # Check output
    print('Checking output folder...')
    if os.path.isdir(output_zip_folder):
        if not force_unzip:
            print('No need to unzip. Skipping...')
            return
        print(f'Removing {output_zip_folder} folder...')
        shutil.rmtree(output_zip_folder)
        print('Done!')
    else:
        print('No need to delete because it does not exist.')

    # Process unzip
    assert input_zip_path.endswith('.zip')
    print('Opening input file...')
    with zipfile.ZipFile(input_zip_path, 'r') as zip_file:
        print(f'Extracting all file from [{input_zip_path}] into [{output_zip_folder}]...')
        zip_file.extractall(output_zip_folder)
    print('Unzipping done!')


def _create(output_zip_folder, images_per_race, dataset_folder):
    # Check dataset folder
    print('Cleaning and/or creating dataset folder...')
    if os.path.isdir(dataset_folder):
        print(f'Removing {dataset_folder} folder...')
        shutil.rmtree(dataset_folder)
    else:
        print('No need to delete because it does not exist.')
    os.makedirs(dataset_folder)
    print('Done!')

    # Create dataset
    assert images_per_race >= 1
    print(f'Iterating over races and getting {images_per_race} per race...')
    for race_folder in glob.glob(os.path.join(output_zip_folder, 'images', 'images', '*')):
        images_list = glob.glob(f'{race_folder}/*.jpg')
        print(f'{race_folder}: {len(images_list)} images')
        for _ in range(min(images_per_race, len(images_list))):
            image_to_use = random.choice(images_list)
            shutil.copy(image_to_use, os.path.join(dataset_folder, image_to_use.split('/')[-1]))
            images_list.remove(image_to_use)
    print('Done!')


def prepare(images_per_race, input_zip_path, output_zip_folder, dataset_folder, force_unzip):
    _unzip(input_zip_path, output_zip_folder, force_unzip)
    _create(output_zip_folder, images_per_race, dataset_folder)


if __name__ == '__main__':
    args = parse_args()
    prepare(args.images_per_race, args.input_zip_path, args.output_zip_folder, args.dataset_folder, args.force_unzip)
