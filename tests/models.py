from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Language(models.Model):
    """ Модель для языков программирования. """
    name = models.CharField('Имя языка', max_length=100)
    about = models.TextField('Описание')
    image = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")

    level = models.ForeignKey(
        'Level', on_delete=models.CASCADE, verbose_name='Уровен')

    def __str__(self):
        return f'{self.name} - {self.level}'

    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'


class Level(models.Model):
    """ Модель для уровня программирования. """
    name = models.CharField('Уровен', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Уровен программирования'
        verbose_name_plural = 'Уровни программирования'


class WrongAnswers(models.Model):
    """ Модель для неправильных ответов. """
    wrong_answer = models.CharField('Неправильный ответ', max_length=255)

    def __str__(self):
        return self.wrong_answer

    class Meta:
        verbose_name = 'Неправильный ответ'
        verbose_name_plural = 'Неправильные ответы'


class Question(models.Model):
    """ Модель для вопроса. """
    question = models.CharField('Вопрос', max_length=255)
    right_answer = models.CharField('Правильный ответ', max_length=255)
    wrong_answers = models.ManyToManyField(
        WrongAnswers, verbose_name='Неправильные ответы')

    language = models.ForeignKey(
        Language, on_delete=models.CASCADE, verbose_name='Язык программирования')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Result(models.Model):
    """ Модель для результата пользователей. """
    right_answers = models.PositiveSmallIntegerField('Результат')
    duration = models.DurationField('Продолжительность')
    data = models.DateTimeField('Дата ',auto_now_add=True)

    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name='Язык')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользовател')

    def __str__(self):
        return f'{self.user}` ответил на {self.right_answers} правильных вопросов'

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'
