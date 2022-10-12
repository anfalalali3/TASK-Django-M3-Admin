from django.contrib import admin

from .models import Pokemon

# Register your models here.
@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('id','name','active','hp',)
    list_display_links = ('id','name',)
    list_filter = ('active',)

    fieldsets = (
        (
            "general", {
                "fields":("name", "hp","active","type",)  
            }
        ),
        (
            "localizations", {
                "fields":("name_ar", "name_fr", 
                "name_jp",),
                "classes":("collapse",)

            }
            ),
     )



