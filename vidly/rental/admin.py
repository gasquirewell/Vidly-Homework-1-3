from django.contrib import admin
from .models import Genre, Movie

# Register your models here.
class GenreTemplate(admin.ModelAdmin):
    list_display = ("id", "name")

# id,title, release_year, price
# tuple
# python manage.py createsuperuser
class MovieTemplate(admin.ModelAdmin):
    list_display = ("id", "title", "release_year", "price")
    list_display_links = ("id", "title")
    field = ("genre", "date_created","release_year", "title", "director","price", "image_url" "description")
    #exclude = ("price",)


admin.site.register(Genre, GenreTemplate)
admin.site.register(Movie, MovieTemplate)
