import shutil

from src.helper import image
from src.nmslib.nmslib import Nmslib


def build(features, index_file_path):
    print(f'Saving index into {index_file_path}')
    features_numpy_array = image.list_to_numpy_array(features)
    index = Nmslib()
    index.fit(features_numpy_array)
    index.save(index_file_path)
    print('Done!')


def search(features, index_file_path, images_list_path, output_image_path):
    with open(images_list_path, 'r') as f:
        images_list = list(f.read().split('\n'))

    index = Nmslib()
    index.load(index_file_path)
    closest, distances = index.query(features, 1)
    for idx, dist in zip(closest, distances):
        print(f'Image index: [{idx}] - Distance: [{dist}]')
        output_image_path_dataset = images_list[idx]
        shutil.copy(output_image_path_dataset, output_image_path)
        return
