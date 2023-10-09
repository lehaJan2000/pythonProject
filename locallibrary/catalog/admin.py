from django.contrib import admin
from .models import Author, Genre, Book, BookInstance

#admin.site.register(Author)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass


#admin.site.register(Book)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
#admin.site.register(BookInstance)
