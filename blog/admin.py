from django.contrib import admin


from .models import Author, Tag, Post, Comment


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


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "user_email", "post", "text")
    search_fields = ("user_name", "user_email", "text")


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Comment, CommentAdmin)
