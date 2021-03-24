from django.db import models

# 회원관리를 위한 DB 생성 => 회원가입 시 이 DB로 데이터가 넘어오게 처리하기
class Member(models.Model):
    username = models.CharField(max_length=20, verbose_name='아이디', null = True)
    email  = models.EmailField(max_length=50, verbose_name='이메일', null = True)
    password  = models.CharField(max_length=20, verbose_name='비밀번호', null = True)
    nickname = models.CharField('닉네임',  max_length=20, null = True)
    prof_pic = models.ImageField('프로필 사진', upload_to='images/', blank=True, null=True)
    species = models.CharField('반려동물 종', max_length=20, null = True)
    local = models.CharField('지역(구/동)', max_length=20, null = True)

    def __str__(self):
        return self.username