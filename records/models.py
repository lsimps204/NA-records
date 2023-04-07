import uuid
from django.db import models


# Create your models here.
class Record(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=256, null=True)
    citable_reference = models.CharField(max_length=256, null=True)
    description = models.TextField(null=True)


    def __str__(self):
        base_str = f"Record {self.id}"
        if self.title:
            base_str = f"{base_str} with title {self.title}"
        return base_str