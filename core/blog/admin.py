from django.contrib import admin
from .models import Post,Category
# Register your models here.
class Post_admin(admin.ModelAdmin):
    list_display = ["title","status","category","author","created_date","pubished_date"]

admin.site.register(Post,Post_admin)
admin.site.register(Category)