from django.contrib import admin
from webapp.models import Book

# admin.site.register(Book)

# class BookAdmin(admin.ModelAdmin):
#     pass
#
# admin.site.register(Book, BookAdmin)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'author', 'mail')
    list_filter = ('author',)
    search_fields = ('title', 'content')
    fields = ('id', 'title', 'content', 'status', 'author', 'mail', 'created_at', 'updated_at')
    # exclude = []
    readonly_fields = ('id', 'created_at', 'updated_at')
