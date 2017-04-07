from django.core.management.base import BaseCommand

from mapper.base import process_factory
from mapper.processes import ETLProcess
from mapper.extractors import HTTPExtractor
from mapper.loaders import ModelLoader
from habr.etl_process import HabrRSSTransformer


class Command(BaseCommand):

    def handle(self, *args, **options):
        process = process_factory(ETLProcess, HTTPExtractor('https://habrahabr.ru/rss/interesting/'),
                                  HabrRSSTransformer(), ModelLoader())
        process.start()
