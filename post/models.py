from django.db import models # type: ignore

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=250)
    img_link = models.TextField()
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title