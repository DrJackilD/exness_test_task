import csv
from io import StringIO
from unittest import TestCase

from mapper.base import BaseExtractor, BaseTransformer, BaseLoader, process_factory
from mapper.processes import ETLProcess


class TExtractor(BaseExtractor):

    def extract(self):
        return StringIO("a,b\n1,2\n3,4")


class TTransformer(BaseTransformer):

    def transform(self, content):
        reader = csv.reader(content)
        headers = next(reader)
        items = []
        for row in reader:
            item = dict(zip(headers, row))
            items.append(item)
        return items


class TLoader(BaseLoader):

    def load(self, content):
        return content


class TProcess(ETLProcess):

    result = None

    def start(self):
        content = self.extractor.extract()
        content = self.transformer.transform(content)
        self.result = self.loader.load(content)


class MapperTestCase(TestCase):

    def test_etl_process(self):
        process = process_factory(TProcess, TExtractor(), TTransformer(), TLoader())
        process.start()
        self.assertEqual([{'a': '1', 'b': '2'}, {'a': '3', 'b': '4'}], process.result)
