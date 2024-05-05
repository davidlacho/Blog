from django.contrib import admin


from .models import Author, Tag, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "author", "url")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "content")


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email_address")
    search_fields = ("full_name", "email_address")


class TagAdmin(admin.ModelAdmin):
    list_display = ("caption",)
    search_fields = ("caption",)


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Author, AuthorAdmin)
