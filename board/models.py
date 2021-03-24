from django.db import models
from members.models import Member

# 자유게시판
class Post(models.Model):
    author = models.ForeignKey(Member, on_delete=models.CASCADE)
    author_name = models.CharField('작성자', max_length=20)
    p_title = models.CharField('글 제목', max_length=100)
    p_contents = models.CharField('글 내용', max_length=300)
    p_date = models.DateTimeField('글 작성일')
    p_count = models.IntegerField(default=0)

    def __str__(self):
        return self.p_title

# 병원후기 게시판
class Posthr(models.Model):
    author = models.ForeignKey(Member, on_delete=models.CASCADE)
    author_name = models.CharField('작성자', max_length=20)
    phr_title = models.CharField('글 제목', max_length=100)
    phr_contents = models.CharField('글 내용', max_length=300)
    phr_date = models.DateTimeField('글 작성일')
    phr_count = models.IntegerField(default=0)

    def __str__(self):
        return self.contents

# 펫 분실 게시판
class Postps(models.Model):
    author = models.ForeignKey(Member, on_delete=models.CASCADE)
    author_name = models.CharField('작성자', max_length=20)
    pps_title = models.CharField('글 제목', max_length=100)
    pps_contents = models.CharField('글 내용', max_length=300)
    pps_date = models.DateTimeField('글 작성일')
    pps_count = models.IntegerField(default=0)

    def __str__(self):
        return self.contents
