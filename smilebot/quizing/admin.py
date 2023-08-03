from django.contrib import admin
from quizing.models import Quiz,Question,Result,Answer
# Register your models here.
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Result)
admin.site.register(Answer)