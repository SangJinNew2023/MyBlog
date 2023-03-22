from django.contrib import admin
from .models import Question, Answer, Comment
# Register your models here.
admin.site.register(Question, Answer, Comment )
