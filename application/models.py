from django.db import models


class Profession(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание', blank=True)
    image = models.ImageField('Изображение', blank=True, upload_to='profession_img/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'


class RelevancePage(models.Model):

    def __str__(self):
        return 'Востребованность'

    class Meta:
        verbose_name = 'Востребованность'
        verbose_name_plural = 'Востребованность'


class GeoPage(models.Model):

    def __str__(self):
        return 'География'

    class Meta:
        verbose_name = 'География'
        verbose_name_plural = 'География'


class SkillPage(models.Model):

    def __str__(self):
        return 'Навыки'

    class Meta:
        verbose_name = 'Навыки'
        verbose_name_plural = 'Навыки'


class Element(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    csv_file = models.FileField('Файл .csv', upload_to='csv/', blank=True)
    img_file = models.ImageField('График', upload_to='charts/')

    relevance_id = models.ForeignKey(RelevancePage, on_delete=models.DO_NOTHING, null=True)
    geo_id = models.ForeignKey(GeoPage, on_delete=models.CASCADE, null=True)
    skill_id = models.ForeignKey(SkillPage, on_delete=models.DO_NOTHING, null=True)

    class Meta:
        verbose_name = 'Элемент'
        verbose_name_plural = 'Элементы'

    def __str__(self):
        return self.title
