from django.contrib import admin

# Register your models here.
from polls.models import Question

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'pub_date')
    list_filter = ("pub_date", )