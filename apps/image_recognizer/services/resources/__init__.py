import os

from apps.image_recognizer.non_database_models import ResourceFile

_FILE_PATH = os.path.dirname(os.path.realpath(__file__))

MODEL_H5_RESOURCE_FILE = ResourceFile(os.path.join(_FILE_PATH, 'model.h5'))
WEIGHTS_H5_RESOURCE_FILE = ResourceFile(os.path.join(_FILE_PATH, 'weights.h5'))