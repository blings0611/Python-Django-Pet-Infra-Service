from django.contrib import admin
from members.models import Member

# models.Model 과 동일하게 admin 에서 ModelAdmin 을 상속
# class BoardMemberAdmin(admin.ModelAdmin):
#     list_display = ('username', 'email', 'password')

admin.site.register(Member)