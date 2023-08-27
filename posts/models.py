import uuid
from django.db import models


class Post(models.Model):
    id = models.UUIDField(
        name='id', primary_key=True,
        null=False, editable=False)
    content = models.TextField(
        name='content',
        null=False, editable=False
    )
    created_at = models.DateTimeField(
        name='created_at',
        auto_now=True, editable=False)

    class Meta:
        db_table = 'post'


# We are going to maintain the analysis in another table following the principle of separation of concerns
class PostAnalysis(models.Model):
    id = models.UUIDField(
        name='id', primary_key=True,
        default=uuid.uuid4, editable=False)
    post = models.OneToOneField(
        name='post_id',
        to=Post, on_delete=models.CASCADE,
        related_name='analysis', related_query_name='post')
    word_count = models.IntegerField(
        name='word_count',
        null=False, editable=False
    )
    average_word_size = models.FloatField(
        name='average_word_size',
        null=False, editable=False
    )
    created_at = models.DateTimeField(
        name='created_at',
        auto_now=True, editable=False)

    class Meta:
        db_table = 'post_has_analysis'
