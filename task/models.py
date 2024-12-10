from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name
    
class Task(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    deadline = models.DateTimeField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.title
