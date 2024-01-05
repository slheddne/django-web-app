from django.contrib import admin

from listings.models import Band, Listing


class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'year_formed',
                    'active')  # liste les champs que nous voulons sur l'affichage de la liste des objets


admin.site.register(Band, BandAdmin)


class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'sold', 'year', 'type', 'band')


admin.site.register(Listing, ListingAdmin)
