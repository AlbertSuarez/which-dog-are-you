from src.helper import image
from src.nmslib.nmslib import Nmslib


def build(features, index_file_path):
    print(f'Saving index into {index_file_path}')
    features_numpy_array = image.list_to_numpy_array(features)
    index = Nmslib()
    index.fit(features_numpy_array)
    index.save(index_file_path)
    print('Done!')
