import numpy as np

from PIL import Image

from src import IMAGE_SIZE


def resize(image_path):
    img = Image.open(image_path).convert('RGB')
    img = img.resize(size=IMAGE_SIZE, resample=Image.LANCZOS)
    return img


def image_to_numpy_array(image_pillow):
    numpy_image = np.array(image_pillow)
    numpy_image = np.expand_dims(numpy_image, axis=0)
    return numpy_image


def list_to_numpy_array(list_object):
    numpy_array = np.array(list_object)
    return numpy_array
