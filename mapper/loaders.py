from django.conf import settings

from mapper.base import BaseLoader


class ModelLoader(BaseLoader):

    def load(self, items):
        for item in items:
            for model in item:
                model.save()
