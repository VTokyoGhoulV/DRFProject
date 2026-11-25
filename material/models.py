from django.db import models


class Course(models.Model):
    name = models.CharField()
    preview = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    name = models.CharField()
    description = models.TextField()
    preview_image = models.ImageField(upload_to='lesson/preview_image')
    video_url = models.URLField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
