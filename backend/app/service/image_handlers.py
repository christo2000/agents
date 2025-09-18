import base64


class ImageReader:
    def reader(self):
        pass

class FileImageReader(ImageReader):
    def __init__(self, path):
        self.path = path

    def reader(self):
        with open(self.path, "rb") as img:
            return img.read()

class ImageToBase64:
    def __init__(self, reader:FileImageReader):
        self.reader = reader
    def encode(self):
        return base64.b64encode(self.reader.reader()).decode('utf-8')
