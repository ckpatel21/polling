from django.contrib import admin

# Register your models here.
from .models import Questions,Choice

admin.site.site_header = "Pollstar Admin"
admin.site.site_header = "Pollstar Admin Area"
admin.site.site_header = "Wellcome to Pollstar Admin area"

class ChoiceInline(admin.TabularInline):
    model=Choice
    extra=3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None,{'fields':['question_text']})
    ,('Date Information',{'fields':['pub_date'],'classes':['collapase']})
    ,]
    inlines = [ChoiceInline]

#admin.site.register(Questions)
#admin.site.register(Choice)\

admin.site.register(Questions,QuestionAdmin)