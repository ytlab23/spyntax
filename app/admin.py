# from django.contrib import admin
# from .models import Url

# admin.site.register(Url)
from .forms import TextForm
from .models import Url, Text
from django.contrib import admin
from django.contrib.admin import TabularInline


class TextInline(TabularInline):
    form = TextForm
    model = Text


class UrlAdmin(admin.ModelAdmin):
    inlines = [TextInline]


admin.site.register(Url, UrlAdmin)
