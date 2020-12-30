from typing import TYPE_CHECKING

import numpy as np
from keras.models import load_model
from keras.preprocessing.image import img_to_array

from apps.image_recognizer.services.resources import MODEL_H5_RESOURCE_FILE, WEIGHTS_H5_RESOURCE_FILE

if TYPE_CHECKING:
    from PIL import Image


class ImageRecognitionService:
    _IMAGE_WIDTH = 256
    _IMAGE_HEIGHT = 256
    _CHARACTERS = {
        0: 'Homer Simpson',
        1: 'Bart Simpson',
        2: 'Marge Simpson'
    }

    def predict(self, image: 'Image.Image') -> str:
        model = load_model(MODEL_H5_RESOURCE_FILE.file_path)
        model.load_weights(WEIGHTS_H5_RESOURCE_FILE.file_path)
        resized_image = image.resize((self._IMAGE_WIDTH, self._IMAGE_HEIGHT))
        img_array = img_to_array(resized_image)
        img_shape = np.expand_dims(img_array, axis=0)
        result = model.predict(img_shape)[0]
        answer = np.argmax(result)
        return self._CHARACTERS[answer]
