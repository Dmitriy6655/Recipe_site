from django.db import models

# from allauth.account.models import EmailAddress

from django.contrib.auth.models import User

from datetime import datetime

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=50, blank=True, verbose_name='Телефон')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'

    def __str__(self):
        return self.user.__str__()

    # def account_verified(self):
    #     if self.user.is_authenticated:
    #         result = EmailAddress.objects.filter(email=self.user.email)
    #         if len(result):
    #             return result[0].verified
    #     return False


class RecipesCategory(models.Model):
    name_category = models.CharField(max_length=100)

    def __str__(self):
        return self.name_category



class Recipes(models.Model):
    name = models.CharField(max_length=200)  # Название рецепта
    description = models.TextField()  # Описание
    cooking_steps = models.TextField()  # Шаги приготовления
    cooking_time = models.IntegerField()  # Время приготовления
    image = models.ImageField(upload_to='image/')
    author = models.CharField(max_length=120)
    date_create = models.DateTimeField(auto_now_add=True)
    recipescategory = models.ForeignKey(RecipesCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'name: {self.name}, description: {self.description}, cooking_steps: {self.cooking_steps}, ' \
               f'cooking_time: {self.cooking_time}, author: {self.author}, date_create {self.date_create} '





class Image(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    image = models.ImageField(upload_to='images/', null=True, max_length=255)

    def __repr__(self):
        return 'Image(%s, %s)' % (self.title, self.image)

    def __str__(self):
        return self.title