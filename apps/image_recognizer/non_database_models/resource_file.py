from pathlib import Path


class ResourceFile:

    @property
    def file_path(self):
        return str(self._file_path)

    def __init__(self, file_path):
        self._file_path = Path(file_path)
