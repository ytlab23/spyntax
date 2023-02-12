from django.db import models


class Url(models.Model):
    url = models.CharField(max_length=32)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url


class Text(models.Model):
    url = models.ForeignKey(Url, on_delete=models.CASCADE)
    text = models.CharField(max_length=5000)

    def __str__(self):
        return self.text
