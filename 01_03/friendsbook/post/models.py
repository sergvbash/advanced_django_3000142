from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.core.exceptions import ValidationError


BAD_WORDS = ['java','waterfall']

def validade_no_bad_words(content):
    if any([word in content.lower() for word in BAD_WORDS]):
        raise ValidationError('This post contain bad words')

class Post(models.Model):
    author = models.ForeignKey(User, null=True, blank=True, on_delete=CASCADE)
    content = models.CharField(max_length=140, validators=[validade_no_bad_words])
    created_on = models.DateTimeField('date created', auto_now_add=True)

    def __str__(self):
        return '{}: {}'.format(self.author, self.content[0:20])