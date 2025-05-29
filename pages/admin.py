from django.contrib import admin
from .models import Page

class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "slug")

admin.site.register(Page, PageAdmin)
