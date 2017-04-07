class BaseExtractor(object):

    def extract(self):
        raise NotImplementedError('You need implement `extract` method for {}'.format(self.__class__.__name__))


class BaseTransformer(object):

    def transform(self, content):
        raise NotImplementedError('You need implement `transform` method for {}'.format(self.__class__.__name__))


class BaseLoader(object):

    def load(self, content):
        raise NotImplementedError('You need implement `load` method for {}'.format(self.__class__.__name__))


class BaseETLProcess(object):

    def start(self):
        raise NotImplementedError('You need implement `start_process` method for {}'.format(self.__class__.__name__))


def process_factory(process, extractor, transformer, loader):
    return process(extractor, transformer, loader)
