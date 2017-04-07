from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50, primary_key=True, unique=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    ts = models.DateTimeField('Date Published', 'ts')
    link = models.CharField(max_length=200, primary_key=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)

    def __str__(self):
        return '[{}] {} - {}'.format(self.ts, self.author.name, self.title)
