import os


class FileSpider:

    def __init__(self, path):
        self.path = path

    @property
    def listdir(self):
        return os.listdir(self.path)

    @property
    def html_pages(self):
        return [i for i in self.listdir if i.endswith(".html")]

