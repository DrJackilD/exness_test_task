from mapper.base import BaseETLProcess


class ETLProcess(BaseETLProcess):

    def __init__(self, ext, trans, load):
        self.extractor = ext
        self.transformer = trans
        self.loader = load

    def start(self):
        content = self.extractor.extract()
        content = self.transformer.transform(content)
        self.loader.load(content)
