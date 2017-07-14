from django.db import models


# Create your models here.

class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回主题"""
        return self.text


class Entry(models.Model):
    """学到的有关主题的具体知识"""
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回知识的内容"""
        if len(self.text) > 500:
            return self.text[:50] + "..."
        else:
            return self.text
