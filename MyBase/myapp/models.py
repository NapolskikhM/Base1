from django.db import models


class Table1(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    age = models.IntegerField(default=0, verbose_name='Возраст')
    description = models.CharField(max_length=50, verbose_name='Должность')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Работники'
        verbose_name_plural = 'Работники'


class Table2(models.Model):
    range = models.CharField(max_length=50, verbose_name='Звание')
    age = models.IntegerField(default=0, verbose_name='Возраст')
    qualification = models.CharField(max_length=50, verbose_name='квалификация')

    def __str__(self):
        return self.range

    class Meta:
        verbose_name = 'Специалисты'
        verbose_name_plural = 'Специалисты'


class Table3(models.Model):
    name = models.ForeignKey(Table1, on_delete=models.CASCADE)
    exp = models.IntegerField(default=0, verbose_name='Опыт')

    '''def __str__(self):
        return self.name'''

    class Meta:
        verbose_name = 'Имя'
        verbose_name_plural = 'Имя'


class Table4(models.Model):
    name = models.ForeignKey(Table1, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0, verbose_name='Зарплата')

    '''def __str__(self):
        return self.name'''

    class Meta:
        verbose_name = 'Зарплата'
        verbose_name_plural = 'Зарплата'


