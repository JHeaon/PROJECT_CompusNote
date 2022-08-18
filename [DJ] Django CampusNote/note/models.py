from django.db import models

# Create your models here.


class user(models.Model):

    user_id = models.CharField(max_length=10)
    user_pwd = models.CharField(max_length=20)
    user_nickname = models.CharField(max_length=20)
    user_name = models.CharField(max_length=10)
    user_university = models.CharField(max_length=30)
    user_e_mail = models.CharField(max_length=40)
    user_phonenumber = models.CharField(max_length=15)
    user_shop = models.CharField(max_length=15, default=" ")
    user_money = models.IntegerField(default=0)

    def __str__(self):
        return self.user_name


class Post(models.Model):

    title = models.CharField(max_length=30)
    content = models.TextField()
    tag = models.CharField(max_length=30)
    file = models.FileField()
    dt_created = models.DateTimeField(
        verbose_name="Date Created", auto_now_add=True)

    def __str__(self):
        return self.title


class QAPost(models.Model):

    title = models.CharField(max_length=30)
    content = models.TextField()
    tag = models.CharField(max_length=30)
    file = models.FileField()
    dt_created = models.DateTimeField(
        verbose_name="Date Created", auto_now_add=True)

    def __str__(self):
        return self.title


class Subject(models.Model):

    title = models.CharField(max_length=30)
    professor = models.CharField(max_length=30)
    star = models.BooleanField(default=False)


class Shop(models.Model):
    title = models.CharField(max_length=30)
    price = models.CharField(max_length=6)
    content = models.TextField()
    tag = models.CharField(max_length=30)
    file = models.FileField()

    def __str__(self):
        return self.title
