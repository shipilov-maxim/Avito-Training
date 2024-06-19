from djongo import models


class Secret(models.Model):
    _id = models.ObjectIdField()
    message = models.TextField(max_length=1000)
    password = models.CharField(max_length=1000, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.created_at
