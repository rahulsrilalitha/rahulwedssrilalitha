from django.db import models
from django.utils.safestring import mark_safe


class Engagement(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/engagement/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def image_tag(self):  # new
        return mark_safe('<img src="/../../media/%s" width="150" height="150" />' % (self.image))

    def __str__(self):
        return self.title
