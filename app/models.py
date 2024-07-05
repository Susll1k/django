from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name='Курс'
        verbose_name_plural='Курсы'


class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    surname = models.CharField(max_length=100, verbose_name='Фамилия')
    age = models.IntegerField(verbose_name='Возраст')
    courses = models.ManyToManyField(Course, related_name='students')  
    def __str__(self):
        return f'{self.surname} {self.name}'
    
    class Meta:
        verbose_name='Студент'
        verbose_name_plural='Студенты'

