from django.db import models


class Quote(object):

    def __init__(self, character, line, sketch):
        self.character = character
        self.line = line
        self.sketch = sketch


class Snippet(models.Model):

    title = models.CharField(max_length=80)
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(max_length=80, default='python')

    class Meta:
        app_label = 'test_app'
