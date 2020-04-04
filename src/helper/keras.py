from keras.applications import InceptionV3

from src import IMAGE_SIZE, IMAGE_CHANNELS
from src.helper import image


resnet50_model = InceptionV3(
    include_top=False,
    input_shape=IMAGE_SIZE + (IMAGE_CHANNELS,),
    pooling='avg',
    weights='imagenet'
)


def extract_features(images, images_list_path):
    features = list()
    images_list = list()
    for idx, image_path in enumerate(images):
        print(f'({idx + 1}/{len(images)}: {image_path}')
        image_pillow = image.resize(image_path)
        image_input = image.image_to_numpy_array(image_pillow)
        if image_input is not None:
            feature_array = resnet50_model.predict(image_input)
            feature_array = feature_array[0]
            features.append(list(feature_array))
            images_list.append(image_path)
        image_pillow.close()
    print('Done!')
    print(f'Saving image list into {images_list_path}...')
    with open(images_list_path, 'w') as f:
        f.write('\n'.join(images_list))
    print('Done!')
    return features
