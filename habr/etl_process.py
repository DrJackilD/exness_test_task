import datetime

from lxml import etree

from mapper.base import BaseTransformer
from habr.models import Author, Article


class HabrRSSTransformer(BaseTransformer):

    def transform(self, content):
        items = []
        tree = etree.fromstring(content.encode())
        for row in tree.xpath('//item'):
            author = Author(**{
                'name': row.xpath('.//dc:creator//text()', namespaces={'dc': 'http://purl.org/dc/elements/1.1/'})[0]
            })
            article = Article(**{
                'title': row.xpath('.//title/text()')[0],
                'description': row.xpath('.//description/text()')[0],
                'ts': datetime.datetime.strptime(row.xpath('.//pubDate/text()')[0],
                                                 '%a, %d %b %Y %H:%M:%S %Z'),
                'author': author,
                'link': row.xpath('.//guid/text()')[0]
            })
            items.append((author, article))
        return items
