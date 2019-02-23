import abc


class PhotoUploader(abc.ABC):
    """This class is used as the base class for uploading photos."""

    @abc.abstractmethod
    def write(self, filename, file):
        pass

    @abc.abstractmethod
    def read(self, key):
        pass
