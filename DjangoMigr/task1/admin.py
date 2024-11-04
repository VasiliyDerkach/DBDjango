from django.contrib import admin
from .models import Post, Game
# Register your models here.
# admin.site.registr('Post')
# admin.site.registr('Game')
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','content',)
    search_fields = ('title',)

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title','cost','size','description','age_limited')
    search_fields = ('title','cost','size','description','age_limited')