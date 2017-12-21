from django.contrib import admin
from .models import Post

# Register your models here.

#naming thik rakhba bojhar subidharthe
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date', 'published_date')
    search_fields = ('title',)

admin.site.register(Post, PostAdmin)


