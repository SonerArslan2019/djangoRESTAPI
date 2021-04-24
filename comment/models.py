from django.contrib.auth.models import User
from django.db import models
from post.models import Post


class Comment( models.Model ):
    user = models.ForeignKey( User, on_delete=models.CASCADE )
    post = models.ForeignKey( Post, on_delete=models.CASCADE )
