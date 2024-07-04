from django.contrib import admin

from .models import Recipes

from django.contrib import admin

from .models import Recipes, Category


class RecipesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'step', 'time', 'is_published')
    list_display_links = ('id', 'title') #Ссылки
    search_fields = ('title', 'content') # по каким полям будет поиск
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title') #Ссылки
    search_fields = ('title',) # по каким полям будет


admin.site.register(Recipes, RecipesAdmin)
admin.site.register(Category, CategoryAdmin)



