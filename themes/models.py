from django.db import models

class Local(models.Model):
    title = models.CharField('이름', max_length=200)
    venue = models.CharField('주소', max_length=200)
    category = models.CharField('카테고리', max_length=200)
    tel = models.CharField('전화번호', max_length=200)
    img_url = models.URLField('썸네일 URL', max_length=400, blank=True)

    def __str__(self):
        return self.title
