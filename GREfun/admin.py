from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from GREfun.models import Word,Meaning,Question,Student

# Register your models here.
admin.site.register(Word)
admin.site.register(Meaning)
admin.site.register(Question)

class StudentInline(admin.StackedInline):
	model = Student
	verbose_name_plural = ' student '

class UserAdmin(UserAdmin):
	inlines = (StudentInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)