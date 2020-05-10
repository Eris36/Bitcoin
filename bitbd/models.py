from django.db import models
from django.utils import timezone





class Post(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    name = models.TextField()
    price = models.TextField()

    def publish(self):
        self.published_data = timezone.now()
        self.save()


