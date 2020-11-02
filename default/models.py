from django.db import models

# Create your models here.


class Poll(models.Model):
    subject = models.CharField(max_length=200, verbose_name='Polling Subject')
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + ")" + self.subject


class Option(models.Model):

    poll_id = models.IntegerField()

    title = models.CharField(max_length=200, verbose_name='Vote Option')

    count = models.IntegerField(default=0)

    #def __str__(self):
    #    return str(self.id) + ")" + self.title

    def __str__(self):
        return str(self.id) + ")" + self.title